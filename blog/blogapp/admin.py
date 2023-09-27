from django.contrib import admin
from .models import Product
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['name','cat','price','status']

    #filters by category and status
    list_filter=['cat','status']
admin.site.register(Product,AdminProduct)

#for changing header name
admin.site.site_header="Ecommerce Dashboard"

#for changing title
admin.site.site_title="Ecommerce"

#for index title
admin.site.index_title="Ecommerce Administration"