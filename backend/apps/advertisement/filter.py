from django_filters import rest_framework as filters

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class AdvertisementFilter(filters.FilterSet):
    # Діапазон ціни
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price = NumberInFilter(field_name='price',lookup_expr='in')  # точне значення

    # Рік авто
    car_year = filters.NumberFilter(field_name='car_year')
    car_year__gte = filters.NumberFilter(field_name='car_year', lookup_expr='gte')
    car_year__lte = filters.NumberFilter(field_name='car_year', lookup_expr='lte')

    # Кількість переглядів
    watches = filters.NumberFilter(field_name='watches')
    watches__gt = filters.NumberFilter(field_name='watches', lookup_expr='gt')

    # Кількість невдалих перевірок
    failed_checks = filters.NumberFilter(field_name='failed_checks')
    failed_checks__gt = filters.NumberFilter(field_name='failed_checks', lookup_expr='gt')

    # Регіон, тип, бренд, модель, статус — часткове співпадіння
    region = filters.CharFilter(field_name='region', lookup_expr='icontains')
    type = filters.CharFilter(field_name='type', lookup_expr='icontains')
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    model_of_car = filters.CharFilter(field_name='model_of_car', lookup_expr='icontains')
    advertisement_status = filters.CharFilter(field_name='advertisement_status', lookup_expr='icontains')

    # Опис — часткове співпадіння
    description_of_car = filters.CharFilter(field_name='description_of_car', lookup_expr='icontains')

    # Фільтр за ID продавця
    seller_id = filters.NumberFilter(field_name='seller__id')

    # Фільтр за email або ім’ям продавця
    seller_email = filters.CharFilter(field_name='seller__email', lookup_expr='icontains')
    seller_username = filters.CharFilter(field_name='seller__username', lookup_expr='icontains')

    # Фільтр за ID автосалону
    dealership_id = filters.NumberFilter(field_name='dealership__id')

    # Пошук за назвою автосалону (якщо модель DealershipModel має таке поле)
    dealership_name = filters.CharFilter(field_name='dealership__name', lookup_expr='icontains')

    # Сортування
    order = filters.OrderingFilter(
        fields=(
            'id',
            'price',
            'car_year',
            'watches',
            'failed_checks',
        ),
        field_labels={
            'price': 'Price',
            'car_year': 'Year',
            'watches': 'Views',
        }
    )

