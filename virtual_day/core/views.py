from rest_framework import viewsets
from virtual_day.core.models import Billboard
from virtual_day.users.permissions import IsStudent
from .serializers import (BillboardListSerializer, BillboardDetailSerializer,)
from virtual_day.utils.decorators import query_debugger


class BillboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Billboard.objects.all()
    permission_classes = (IsStudent,)
    serializer_class = BillboardListSerializer

    @query_debugger
    def get_queryset(self):
        billboard_id = self.request.query_params.get('billboard_id', None)
        if billboard_id:
            queryset = Billboard.objects.filter(id=billboard_id)
            self.serializer_class = BillboardDetailSerializer
        else:
            queryset = Billboard.objects.filter(enable=True)
        return queryset
