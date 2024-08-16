from django.urls import path
from .views import get_unique_manufacturer_ids

urlpatterns = [
    path('manufacturers/<int:contract_id>/', get_unique_manufacturer_ids, name='get_unique_manufacturer_ids'),
]