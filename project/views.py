from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from .models import *
from .serializers import *
from common.api.utils import *

# Create your views here.
class ProjectMgr(ViewSetMixin, APIView):
    def list_project(self, request, *args, **kwargs):
        project_list = Project.objects.all()
        ret = ProjectSerializer(project_list, many=True)
        return APIV1OKJsonResponse(data=ret.data)