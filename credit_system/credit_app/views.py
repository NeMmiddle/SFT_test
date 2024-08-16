from django.http import JsonResponse
from .models import Manufacturer


def get_unique_manufacturer_ids(request, contract_id):
    try:
        # Получение уникальных ID производителей для товаров, связанных с заданным контрактом
        manufacturer_ids = Manufacturer.objects.filter(
            products__credit_application__contract__id=contract_id
        ).values_list('id', flat=True).distinct()

        return JsonResponse({'manufacturer_ids': list(manufacturer_ids)})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)