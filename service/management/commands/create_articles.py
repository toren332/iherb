from django.core.management.base import BaseCommand
from service import models
import os
import json
from tqdm import tqdm
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Article.objects.all().delete()
        df = pd.read_excel('iherb.xlsx', index_col=0)
        for index, row in df.iterrows():
            # print(index)
            drug_name = index
            name = f"Статья о {drug_name}"
            rating = row['rating']
            link = row['link']
            a = models.Article.objects.create(link=link, name=name, rating=rating)
            for i in models.Drug.objects.filter(name__contains=drug_name):
                i.articles.add(a)