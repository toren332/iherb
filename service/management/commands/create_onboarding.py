from django.core.management.base import BaseCommand
from service import models
import os
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Drug.objects.all().delete()
        models.Bad.objects.all().delete()
        for i in os.listdir('items'):
            with open(f'items/{i}', 'r') as f:
                data = json.load(f)
            drug_models = []
            categories = data['categories']
            new_categories = []
            for c in categories:
                for k in c.split('\n'):
                    new_categories.append(k)
            new_categories = list(set(new_categories))
            data['categories'] = new_categories
            for drug in data.get('drug_count', []):
                drug_model, created = models.Drug.objects.get_or_create(name=drug)
                drug_models.append(drug_model)
            d = models.Bad.objects.create(**data)
            d.drugs.add(*drug_models)

