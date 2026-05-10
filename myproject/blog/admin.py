from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content',)
    list_filter = ('title', 'content', 'created_at')
    search_fields = ('title', 'content',)