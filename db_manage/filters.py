from django_filters import rest_framework as filters
from db_manage.models import DBmanageModel

class DBmanageModelFilter(filters.FilterSet):

    class Meta:
        model = DBmanageModel
        fields = ['plans_tablename']


























