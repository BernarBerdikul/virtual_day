from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .schedule.views import EventViewSet
from .profile.views import ProfileViewSet

app_name = 'api_client'

router = DefaultRouter()

router.register('profile', ProfileViewSet, basename='profile')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('schedule', EventViewSet, basename='schedule')

urlpatterns = router.urls
