from rest_framework import pagination
from rest_framework.response import Response


class DFPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_num"

    def get_paginated_response(self, data):
        return Response(
            {
                "total_count": self.page.paginator.count,
                "data": data,
                "current": self.page.number,
                "page_num": self.get_page_size(request=self.request),
            }
        )
