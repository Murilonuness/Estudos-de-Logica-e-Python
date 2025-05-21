from django.contrib import admin

from.models import Category, Color, Size, Mark, Product, ProductAttribute

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Mark)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'markProduct', 'colorProduct', 'sizeProduct', 'status')
    list_editable=('status',)
admin.site.register(Product,ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price')

admin.site.register(ProductAttribute,ProductAttributeAdmin)
