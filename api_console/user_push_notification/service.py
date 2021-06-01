from django.db.models import Q
from virtual_day.utils import messages, constants
from virtual_day.utils.exceptions import CommonException
from virtual_day.users.models import User
from firebase import FCMManager as fcm
import time


def send_push_now(push: object) -> None:
    users = User.objects.exclude(
        Q(role=constants.SUPER_ADMIN) & Q(role=constants.ADMIN))
    token_list = [user.firebase_token for user in users]
    response = fcm.sendPush(title=push.title,
                            msg=push.description,
                            image=push.image_path,
                            registration_token=token_list,
                            data_object=push.data)
    push.response = {
        "message_id": response.responses,
        "success_count": response.success_count,
        "failure_count": response.failure_count
    }
    push.date_publication = int(time.time())
    push.is_sent = True
    push.save()
    return None


def check_push_is_not_sent(push: object) -> object:
    """ check if push already sent, even is true, than raise exception """
    if push.is_sent is True:
        raise CommonException(
            detail=messages.RESTAURANT_PUSH_ALREADY_SENT)
    return push


def calculate_pushes_info(push_notification: object) -> object:
    users = User.objects.filter(
        Q(role=constants.STUDENT) | Q(role=constants.MODERATOR))
    user_ids = [user.id for user in users]
    push_notification.users_count = users.count()
    push_notification.user_ids = user_ids
    push_notification.data = {
        "id_push": str(push_notification.id),
        "user_ids": user_ids
    }
    push_notification.save()
    return push_notification
