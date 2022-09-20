from rest_framework import viewsets
from data_verification.models import DataVerificationModel
from rest_framework.response import Response
from data_verification.serializers import DataVerificationSerializers
from common.api.utils import ApiResponse
from rest_framework import status
from common.api.utils import ApiErrorResponse
from data_verification.filters import DataVerificationModelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from data_verification.data_pagination import DataPaginations


# Create your views here.
class DataVerification(viewsets.ViewSet):

    def list(self,request):
        queryset = DataVerificationModel.objects.all()
        if queryset.count()>0:
            res = True
        else:
            res = False
        serializer = DataVerificationSerializers(queryset, many=True)
        return ApiResponse(success=res,data=serializer.data)

    def create(self,request):
        queryset = DataVerificationModel.objects.all()
        if queryset.count()>0:
            res = True
        else:
            res = False
        serializer = DataVerificationSerializers(queryset, many=True)
        return ApiResponse(success=res,data=serializer.data)

class DataVerificationModelViewSet(viewsets.ModelViewSet):

    serializer_class = DataVerificationSerializers
    queryset = DataVerificationModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DataVerificationModelFilter
    pagination_class = DataPaginations
    

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return  ApiResponse(success=True,data=[f'successfully created {len(serializer.data)} records'], errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])

    def destroy(self, request, *args, **kwargs):
        try:
            datas_id = [data['id'] for data in request.data]
            instance = DataVerificationModel.objects.filter(pk__in=datas_id).delete()
            # self.perform_destroy(instance)
            return ApiResponse(success=True,data=[f'successfully deleted {len(datas_id)} records'],errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            datas_id = [data['id'] for data in request.data]
            instance = DataVerificationModel.objects.filter(pk__in=datas_id)
            serializer = self.get_serializer(instance, data=request.data, partial=partial,many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            return ApiResponse(success=True,data=[f'successfully updated {len(serializer.data)} records'], errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])



