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
            for drug in data.get('drug_count', []):
                drug_model, created = models.Drug.objects.get_or_create(name=drug)
                drug_models.append(drug_model)
            d = models.Bad.objects.create(**data)
            d.drugs.add(*drug_models)

