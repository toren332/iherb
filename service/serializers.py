from rest_framework import serializers
from service.models import Article, Drug, Bad


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Drug
        fields = '__all__'


class BadSerializer(serializers.ModelSerializer):
    drugs = DrugSerializer(many=True)

    class Meta:
        model = Bad
        fields = '__all__'


