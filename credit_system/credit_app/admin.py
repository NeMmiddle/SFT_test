from django.contrib import admin
from .models import Manufacturer, Product, Contract, CreditApplication

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(CreditApplication)