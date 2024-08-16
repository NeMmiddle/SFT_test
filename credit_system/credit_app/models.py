from django.db import models
from uuid import uuid4


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Производитель {self.name}"


class Contract(models.Model):
    contract_number = models.CharField(max_length=100, unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Контракт {self.contract_number}"


class CreditApplication(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_application')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Кредитная заявка {self.id}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Продукт {self.name}"
