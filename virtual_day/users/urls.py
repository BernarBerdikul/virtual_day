from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = 'user'

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls
