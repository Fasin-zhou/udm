from django_filters import rest_framework as filters
from cases.models import CasesModel

class CasesModelFilter(filters.FilterSet):
    # blind_numbering = filters.NumberFilter(field_name="blind_numbering")
    # quantity_check = filters.CharFilter(field_name="quantity_check")

    class Meta:
        model = CasesModel
        fields = ['id','exam_hospital','hospital_code','exam_datetime','file_path','batch_number','study_code']


























