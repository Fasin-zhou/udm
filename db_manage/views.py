from rest_framework import viewsets
from db_manage.models import DBmanageModel
from rest_framework.response import Response
from db_manage.serializers import DBmanageModelSerializers
from common.api.utils import ApiResponse
from rest_framework import status
from common.api.utils import ApiErrorResponse
from db_manage.filters import DBmanageModelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from plans.models import PlansModel

# Create your views here.
class DBmanageModelViewSet(viewsets.ModelViewSet):

    serializer_class = DBmanageModelSerializers
    queryset = DBmanageModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DBmanageModelFilter

    def list(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset.count()>0:
            res = True
        else:
            res = False
        serializer = DBmanageModelSerializers(queryset, many=True)
        return ApiResponse(success=res,data=serializer.data, errorCode=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        
        id = request.data.get('id')
        try:
            partial = kwargs.pop('partial', False)
            instance = DBmanageModel.objects.get(pk=id)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            p1 = PlansModel()
            p1.set_db_table()
            return ApiResponse(success=True,data=[serializer.data], errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])

    def destroy(self, request, *args, **kwargs):
        id = request.data.get('id')
        try:
            instance = DBmanageModel.objects.get(pk=id)
            self.perform_destroy(instance)
            return ApiResponse(success=True,data=[{'id':id}],errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])


