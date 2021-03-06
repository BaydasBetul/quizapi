from rest_framework.pagination import PageNumberPagination, CursorPagination


# class SmallPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param="sayfa"
    
    
class PageNumberPagination(PageNumberPagination):
    page_size = 1
    

class MycursorPagination(CursorPagination):
    page_size=3
    ordering = "difficulty"