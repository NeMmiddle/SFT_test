import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from uuid import uuid4
from credit_app.models import Manufacturer, Contract, CreditApplication, Product


class Command(BaseCommand):
    help = 'Проверка, пусты ли таблицы и заполнение их данными, если они есть.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        if CreditApplication.objects.exists():
            self.stdout.write(self.style.SUCCESS('Таблиц уже содержат данные.'))
            return

        # Создаем производителей
        manufacturers = [Manufacturer.objects.create(name=fake.company()) for _ in range(50)]

        # Создаем контракты
        contracts = [Contract.objects.create(contract_number=str(uuid4())) for _ in range(50)]

        with transaction.atomic():
            credit_applications = []
            for contract in contracts:
                credit_application = CreditApplication.objects.create(
                    contract=contract
                )
                credit_applications.append(credit_application)

            for credit_application in credit_applications:
                # Рандомное количество продуктов от 1 до 10
                num_products = random.randint(1, 10)
                products = [
                    Product(
                        name=fake.word(),
                        manufacturer=random.choice(manufacturers),
                        credit_application=credit_application
                    )
                    for _ in range(num_products)
                ]
                Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными.'))
