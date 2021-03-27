from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .schedule.views import ScheduleViewSet
from .user.views import UserViewSet

app_name = 'api_client'

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('schedule', ScheduleViewSet, basename='schedule')

urlpatterns = router.urls
