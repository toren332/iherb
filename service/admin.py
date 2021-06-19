from django.contrib import admin
from service import models
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'rating',]


@admin.register(models.Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


@admin.register(models.Bad)
class BadAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = ['id', 'name', 'img', 'thumb']
    readonly_fields = ('thumb',)

    @staticmethod
    def thumb(obj):
        return mark_safe(f"<img src='{obj.img}'  width='50' height='50' />")


