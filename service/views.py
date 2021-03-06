from rest_framework import viewsets
from service.serializers import BadSerializer
from service.models import Article, Drug, Bad
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


def fuck_data(data):
    for i in data:
        drug_count = i.pop('drug_count')
        el_drugs = i['drugs']
        drugs_rating = []
        for j in el_drugs:
            articles_rating = []
            j['count'] = drug_count.get(j['name'], '-')
            for k in j['articles']:
                articles_rating.append(k['rating'])
            try:
                j['rating'] = sum(articles_rating)/len(articles_rating)
            except:
                j['rating'] = None
            drugs_rating.append(j['rating'])
        drugs_rating = [x for x in drugs_rating if x is not None]
        try:
            i['rating'] = sum(drugs_rating) / len(drugs_rating)
        except:
            i['rating'] = None
    return data


class BadViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BadSerializer
    queryset = Bad.objects.all().order_by('pk')
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = self.queryset
        category = self.request.GET.get('category')
        drug = self.request.GET.get('drug')
        q = self.request.GET.get('q')
        code = self.request.GET.get('code')
        if category is not None:
            qs = qs.filter(categories__contains=[category])
        if drug is not None:
            qs = qs.filter(drugs__name__contains=drug)
        if q is not None:
            qs = qs.filter(name__contains=q)
        if code is not None:
            qs = qs.filter(qcode=code)
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(fuck_data(data))

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(fuck_data(data))


class DrugKinds(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        ac = request.GET.get('ac')
        # data = Drug.objects.values_list('name', flat=True).distinct()
        # with open('drug_kinds.json', 'w') as f:
        #     json.dump(list(data) ,f, ensure_ascii=False, indent=4)
        with open('drug_kinds.json', 'r') as f:
            data = json.load(f)
        if ac is not None:
            data = [x for x in data if x[:len(ac)].lower()==ac.lower()]
        return Response(sorted(data), status=status.HTTP_200_OK)


class CategoriesKinds(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        ac = request.GET.get('ac')
        data = list(set([item for sublist in Bad.objects.values_list('categories', flat=True).distinct() for item in sublist]))
        if ac is not None:
            data = [x for x in data if x[:len(ac)].lower() == ac.lower()]
        return Response(sorted(data), status=status.HTTP_200_OK)

