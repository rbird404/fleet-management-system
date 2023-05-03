from django_filters import rest_framework as filters


class BaseFilterSet(filters.FilterSet):
    def filter_queryset(self, queryset):
        if (
            self.request.user.is_superuser or self.request.user.is_staff
        ):
            return queryset
        return queryset.active()
