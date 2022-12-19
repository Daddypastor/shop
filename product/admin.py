from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display=('name','ref','vendor','category','brand','new','top_deals')
	list_editable=('new','top_deals')
admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
	list_display=('product','stock_status','size','price','discount')
admin.site.register(Variation,VariationAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','rating')
admin.site.register(Review,ReviewAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	list_display=('product','image_tag')
admin.site.register(ProductImage,ProductImageAdmin)

admin.site.register(ProductInformation)

admin.site.register(ExcelcartReview)

