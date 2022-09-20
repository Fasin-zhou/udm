from sre_constants import SUCCESS
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from django.contrib.auth.models import User
from common.api.utils import ApiResponse
from rest_framework import status

# Create your views here.
def password_check(login_password,true_password):
    res = check_password(login_password,true_password)
    return res


class UserLogin(viewsets.ViewSet):
    """
    test/test123.
    admin/admin123
    """

    def list(self,request):
        print(request.user.is_authenticated)
        username = request.GET.get('name')
        login_password = request.GET.get('password')
        queryset = User.objects.filter(username=username)
        if queryset.count()!=1:
            true_password = ''
        else:
            true_password = queryset.values()[0].get('password')
        res = password_check(login_password,true_password)
        # serializer = UserSerializers(queryset, many=True)
        return ApiResponse(success=res,errorCode=status.HTTP_200_OK)
