import django_filters
from django.db.models import Q

from main.models import Doctor


class DoctorFilter(django_filters.FilterSet):
    pk = django_filters.CharFilter(field_name='pk')
    name = django_filters.CharFilter(method="filter_name")
    spec = django_filters.CharFilter(method="filter_spec")

    class Meta:
        model = Doctor
        fields = ['pk', 'name', 'spec', 'number', 'online_pay', 'week_days']

    def filter_name(self, queryset, field, value):
        return queryset.filter(Q(user__first_name__icontains=value) | Q(user__last_name__icontains=value))

    def filter_spec(self, queryset, field, value):
        return queryset.filter(spec=value)
