import sched
import time
from functools import wraps
from threading import Thread
from django.db.models import Q
import FCMManager as fcm
from virtual_day.utils.decorators import query_debugger
from virtual_day.utils import constants


def _async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl
    return async_func


def schedule(interval):
    def decorator(func):
        def periodic(scheduler, interval, action, actionargs=()):
            scheduler.enter(interval, 1, periodic,
                            (scheduler, interval, action, actionargs))
            action(*actionargs)

        @wraps(func)
        def wrap(*args, **kwargs):
            scheduler = sched.scheduler(time.time, time.sleep)
            periodic(scheduler, interval, func)
            scheduler.run()
        return wrap
    return decorator


@_async
@schedule(1)
@query_debugger
def periodic_event():
    from virtual_day.users.models import UserPushNotification, User
    pushes = UserPushNotification.objects.filter(
        date_publication=int(time.time()))
    users = User.objects.filter(is_active=True).filter(
        Q(role=constants.MODERATOR) | Q(role=constants.STUDENT))
    token_list = [user.firebase_token for user in users]
    for push in pushes:
        response = fcm.sendPush(title=push.title,
                                msg=push.description,
                                image=push.image_path,
                                registration_token=token_list,
                                data_object=push.data)
        push.response = {
            "message_id": response.responses[0].message_id,
            "success_count": response.success_count,
            "failure_count": response.failure_count
        }
        push.save()


periodic_event()
