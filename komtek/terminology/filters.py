import django_filters


class GlossaryFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(
        label="Start date",
        field_name="versions__initial_date",
        distinct=True,
        lookup_expr="lte",
    )
