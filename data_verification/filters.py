from django_filters import rest_framework as filters
from data_verification.models import DataVerificationModel

class DataVerificationModelFilter(filters.FilterSet):
    # blind_numbering = filters.NumberFilter(field_name="blind_numbering")
    # quantity_check = filters.CharFilter(field_name="quantity_check")

    class Meta:
        model = DataVerificationModel
        fields = ['data_file_path','blind_numbering','quantity_check']


























