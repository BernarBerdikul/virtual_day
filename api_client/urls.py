from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .event.views import EventViewSet
from .profile.views import ProfileViewSet
from .user.views import UserViewSet

app_name = 'api_client'

router = DefaultRouter()

router.register('profile', ProfileViewSet, basename='profile')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('event', EventViewSet, basename='event')
router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls
