from django.contrib import admin
from ebookapp.models import Category, SubCategory, Book

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Book)

