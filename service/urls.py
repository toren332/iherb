from rest_framework import routers
from django.urls import path
from . import views

app_name = 'iherb'
router = routers.DefaultRouter()

router.register('bads', views.BadViewSet, basename='bads')

urlpatterns = router.urls
urlpatterns += [
    path('drug_kinds/', views.DrugKinds.as_view(), name='drug_kinds'),
    path('category_kinds/', views.CategoriesKinds.as_view(), name='category_kinds'),
]
