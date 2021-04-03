from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .schedule.views import ScheduleViewSet
from .profile.views import ProfileViewSet
from .user.views import UserViewSet
from .user_push_notification.views import UserPushNotificationViewSet

app_name = 'api_console'

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('profile', ProfileViewSet, basename='profile')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('schedule', ScheduleViewSet, basename='schedule')
router.register('push_notification', UserPushNotificationViewSet,
                basename='push_notification')

urlpatterns = router.urls
