"""udm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from login import views
from data_verification.views import DataVerificationModelViewSet
from plans.views import PlansModelViewSet
from cases.views import CasesModelViewSet
from videoplayer.views import stream_video, video_list, ImageFrames
from db_manage.views import DBmanageModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
METHODS_ALL = {"get":"list","post":"create","put":"update","delete":"destroy",}

router = routers.DefaultRouter()
router.register(r'login', views.UserLogin, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/image/', include(('image_annotation.urls', 'image_annotation'), namespace='api-image')),
    path('api/user/', include(('user.urls', 'user'), namespace='api-user')),
    path('api/project/', include(('project.urls', 'project'), namespace='api-project')),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtian_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    path('api/token/verify/',TokenVerifyView.as_view(),name="token_verify"),
    path('date_verification/',DataVerificationModelViewSet.as_view(METHODS_ALL),name="date_verification"),
    path('cases/',CasesModelViewSet.as_view(METHODS_ALL),name="cases"),
    path('plans/',PlansModelViewSet.as_view(METHODS_ALL),name="plans"),
    path('db_manage/',DBmanageModelViewSet.as_view(METHODS_ALL),name="db_manage"),
    path('video_player/',stream_video ,name="video_player"),
    path('video_test/',ImageFrames.as_view() ,name="video_test"),
    path('video_test1/',video_list ,name="video_test1"),
]
