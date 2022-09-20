from django_filters import rest_framework as filters
from plans.models import PlansModel

class PlansModelFilter(filters.FilterSet):

    class Meta:
        model = PlansModel
        fields = ['plans_code','plans_name','plans_begindate','plans_enddate','complete_date','plan_usernumber']


























