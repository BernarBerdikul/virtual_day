from rest_framework.routers import DefaultRouter
from virtual_day.core.views import BillboardViewSet

app_name = 'core'

router = DefaultRouter()

router.register('billboards', BillboardViewSet, basename='billboards')

urlpatterns = router.urls
