from django.contrib import admin

from .models import Post, Category, Location


@admin.register(Post)
class Post(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Category)
class Post(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Location)
class Post(admin.ModelAdmin):
    search_fields = ['name']
