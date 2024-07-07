from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Здесь мы получаем данные из фикстуры с категориями"""
        category_data = []
        with open("fixtures/catalog_data.json") as file:
            file_data = json.load(file)
            for item in file_data:
                if item['model'] == "catalog.category":
                    category_data.append(item)
        return category_data

    @staticmethod
    def json_read_products():
        """Здесь мы получаем данные из фикстуры с продуктами"""
        product_data = []
        with open("fixtures/catalog_data.json") as file:
            file_data = json.load(file)
            for item in file_data:
                if item['model'] == "catalog.product":
                    product_data.append(item)
        return product_data

    def handle(self, *args, **options):
        product_for_create = []
        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category["fields"]['name'], description=category["fields"]['description'], id=category["pk"])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product["fields"]['name'], description=product["fields"]['description'],
                        category=Category.objects.get(id=product["fields"]['category']), price=product["fields"]['price'],
                        created_at=product["fields"]['created_at'], updated_at=product["fields"]['updated_at'], id=product["pk"])
            )
        Product.objects.bulk_create(product_for_create)
