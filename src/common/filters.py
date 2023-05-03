from django_filters import rest_framework as filters


class BaseFilterSet(filters.FilterSet):
    def filter_queryset(self, queryset):
        if (
                not self.request.user.is_superuser
                or not self.request.user.is_staff
        ):
            return queryset
        return queryset.active()
