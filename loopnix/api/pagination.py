from rest_framework import pagination

class UsersPageLOP(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
