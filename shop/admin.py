from django.contrib import admin
from django.db.models.fields import CharField
from . models import *
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(categ,catadmin)


class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','price','stock','img','availabe']
    list_editable=['price','stock','img','availabe']
admin.site.register(products,prodadmin)    