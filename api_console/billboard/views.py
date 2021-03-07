from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from business_service.service_methods import create_translation, update_translation
from virtual_day.core.models import Billboard
from virtual_day.users.permissions import IsAdmin
from .serializers import (BillboardListSerializer, BillboardDetailSerializer,
                          BillboardCreateVideoSerializer, BillboardCreateTextSerializer)
from virtual_day.utils.decorators import query_debugger, except_data_error, response_wrapper
from business_rules.billboard_rules import billboard_rules_response
from virtual_day.utils import constants, codes, messages
from virtual_day.utils.exceptions import CommonException


@method_decorator(response_wrapper(), name='dispatch')
class BillboardViewSet(viewsets.ViewSet):
    permission_classes = (IsAdmin,)
    parser_classes = (MultiPartParser, JSONParser)

    @query_debugger
    def list(self, request):
        billboards = Billboard.objects.all().translate(request.user.language)
        return Response({"model": BillboardListSerializer(billboards, many=True).data,
                         "rules": billboard_rules_response})

    @query_debugger
    def retrieve(self, request, pk=None):
        billboards = Billboard.objects.filter(id=pk).translate(request.user.language)
        billboard = get_object_or_404(billboards, pk=pk)
        return Response(BillboardDetailSerializer(billboard).data)

    @query_debugger
    @except_data_error
    def create(self, request):
        serializer = BillboardDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        billboard = serializer.save()
        if request.data['type'] == constants.TEXT:
            if "pdf_file" not in request.data:
                Billboard.objects.filter(id=billboard.id).delete()
                raise CommonException(code=codes.VALIDATION_ERROR,
                                      detail=messages.WRONG_REQUEST_BODY)
            """ save billboard's pdf_file for text """
            serializer = BillboardCreateTextSerializer(billboard, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        elif request.data['type'] == constants.VIDEO:
            if "url_link" not in request.data:
                Billboard.objects.filter(id=billboard.id).delete()
                raise CommonException(code=codes.VALIDATION_ERROR,
                                      detail=messages.WRONG_REQUEST_BODY)
            """ save billboard's url_link for video """
            serializer = BillboardCreateVideoSerializer(billboard, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        """ create translations """
        create_translation(model=Billboard, translations=request.data['translations'], object_id=billboard.id)
        result_billboard = Billboard.objects.translate(request.user.language).get(id=billboard.id)
        return Response(BillboardListSerializer(result_billboard).data)

    @query_debugger
    @except_data_error
    def partial_update(self, request, pk=None):
        billboards = Billboard.objects.filter(id=pk, enable=True).translate(request.user.language)
        instance = get_object_or_404(billboards, pk=pk)
        serializer = BillboardDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        billboard = serializer.save()
        if request.data['type'] == constants.TEXT:
            if "pdf_file" not in request.data:
                Billboard.objects.filter(id=billboard.id).delete()
                raise CommonException(code=codes.VALIDATION_ERROR,
                                      detail=messages.WRONG_REQUEST_BODY)
            """ save billboard's pdf_file for text """
            serializer = BillboardCreateTextSerializer(billboard, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        elif request.data['type'] == constants.VIDEO:
            if "url_link" not in request.data:
                Billboard.objects.filter(id=billboard.id).delete()
                raise CommonException(code=codes.VALIDATION_ERROR,
                                      detail=messages.WRONG_REQUEST_BODY)
            """ save billboard's url_link for video """
            serializer = BillboardCreateVideoSerializer(billboard, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        """ create translations """
        update_translation(model=Billboard, translations=request.data['translations'], object_id=pk)
        result_billboard = Billboard.objects.translate(request.user.language).get(id=billboard.id)
        return Response(BillboardListSerializer(result_billboard).data)

    @query_debugger
    @except_data_error
    def destroy(self, request, pk=None):
        billboard = Billboard.objects.filter(id=pk)
        get_object_or_404(billboard, pk=pk).delete()
        return Response()
