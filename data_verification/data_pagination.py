from rest_framework import pagination
from common.api.utils import ApiResponse
from data_verification.tasks import add



class DataPaginations(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        if len(data)>0:
            res = True
        else:
            res = False
        add.delay(100,400)
        return ApiResponse(success=res,data=data)
