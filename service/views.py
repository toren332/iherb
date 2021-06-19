from rest_framework import viewsets
from service.serializers import BadSerializer
from service.models import Article, Drug, Bad
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


def fuck_data(data):
    for i in data:
        drug_count = i.pop('drug_count')
        el_drugs = i['drugs']
        for j in el_drugs:
            j['count'] = drug_count.get(j['name'], '-')
    return data


class BadViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BadSerializer
    queryset = Bad.objects.all().order_by('pk')
    pagination_class = StandardResultsSetPagination

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
        return Response(Drug.objects.values_list('name', flat=True).distinct(), status=status.HTTP_200_OK)


class CategoriesKinds(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        data = set([item for sublist in Bad.objects.values_list('categories', flat=True).distinct() for item in sublist])
        return Response(data, status=status.HTTP_200_OK)

