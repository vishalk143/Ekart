from django.contrib import admin
from ecommapp.models import Product
# Register your models here.
# admin.site.register(product)

#define Model admin class
class productAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']

admin.site.register(Product,productAdminClass)
admin.site.site_header="Ekart Dashboard"
