from django_filters import rest_framework as filters


class BaseFilterSet(filters.FilterSet):

    def filter_queryset(self, queryset):
        if (
            self.request.user.is_superuser or self.request.user.is_staff
        ):
            return super().filter_queryset(queryset)
        return super().filter_queryset(queryset.active())


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass
