from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .event.views import EventViewSet
from .profile.views import ProfileViewSet
from .user.views import UserViewSet
from .user_push_notification.views import UserPushNotificationViewSet
from .lecture.views import LectureViewSet
from .dod_day.views import DodDayViewSet

app_name = 'api_console'

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('dod_day', DodDayViewSet, basename='dod_day')
router.register('lecture', LectureViewSet, basename='lecture')
router.register('profile', ProfileViewSet, basename='profile')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('event', EventViewSet, basename='event')
router.register('push_notification', UserPushNotificationViewSet,
                basename='push_notification')

urlpatterns = router.urls
