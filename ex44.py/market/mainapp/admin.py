from django.contrib import admin

from.models import Category, Color, Size, Mark, Product

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Mark)
admin.site.register(Product)