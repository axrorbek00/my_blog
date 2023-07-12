from django.contrib import admin
from .models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
