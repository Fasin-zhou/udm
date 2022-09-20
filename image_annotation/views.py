from rest_framework.views import APIView

from common.api.utils import APIV1OKJsonResponse
from rbac.utils.userPerm import UserPermission


class Image(APIView):
    # authentication_classes = [Auth]
    permission_classes = [UserPermission]
    def get(self, request, *args, **kwargs):
        return APIV1OKJsonResponse('ok')



