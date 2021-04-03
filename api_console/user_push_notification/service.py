from django.db.models import Q
from virtual_day.utils import messages, codes, constants
from virtual_day.utils.exceptions import CommonException
from virtual_day.users.models import User


def check_push_is_not_sent(push: object) -> object:
    """ check if push already sent, even is true, than raise exception """
    if push.is_sent is True:
        raise CommonException(
            detail=messages.RESTAURANT_PUSH_ALREADY_SENT,
            code=codes.BAD_REQUEST)
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
