import base64

from django.contrib import auth
from rest_framework.views import APIView

from .service import *

# Create your views here.
class Login(APIView):
    def post(self, request, *args, **kwargs):
        error_response = APIV1FailJsonResponse(status_code.USER_OR_PWD_ERROR.msg, code=status_code.USER_OR_PWD_ERROR.code)
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        project_id = int(request.data.get('project_id', '0'))
        if is_none(username, password, project_id):
            return APIV1FailJsonResponse(status_code.PARAM_IS_NULL.msg, code=status_code.PARAM_IS_NULL.code)
        elif len(password) < 4:
            # base64 加密后字符串长度最小为4，小于4则密码错误
            return error_response
        user = auth.authenticate(request, username=username, password=base64.b64decode(password))
        if user:
            return login(user, project_id)
        else:
            return error_response

