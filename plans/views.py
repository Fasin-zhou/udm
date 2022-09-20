from rest_framework import viewsets
from plans.models import PlansModel
from rest_framework.response import Response
from plans.serializers import PlansSerializers
from common.api.utils import ApiResponse
from rest_framework import status
from common.api.utils import ApiErrorResponse
from plans.filters import PlansModelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from plans.plans_pagination import PlansPaginations



# Create your views here.
class PlansModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlansSerializers
    queryset = PlansModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlansModelFilter
    pagination_class = PlansPaginations

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
            plans_id = [plan['id'] for plan in request.data]
            instance = PlansModel.objects.filter(pk__in=plans_id).delete()
            # self.perform_destroy(instance)
            return ApiResponse(success=True,data=[f'successfully deleted {len(plans_id)} records'],errorCode=status.HTTP_200_OK)
        except Exception as e:
            return ApiErrorResponse(data=[{'detail':e.__str__()}])

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            plans_id = [plan['id'] for plan in request.data]
            instance = PlansModel.objects.filter(pk__in=plans_id)
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
