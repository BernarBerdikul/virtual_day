from django.urls import path
from rest_framework.routers import DefaultRouter
from .billboard.views import BillboardViewSet
from .schedule.views import ScheduleViewSet
from .user.views import UserViewSet

from .chat.views import (
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    ChatUpdateView,
    ChatDeleteView
)

app_name = 'api_client'

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('billboard', BillboardViewSet, basename='billboard')
router.register('schedule', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view())
]
