from django_filters import rest_framework as filters


class AnalyticsFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name='created')
