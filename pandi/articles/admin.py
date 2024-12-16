from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'is_published')
    list_filter = ('is_published', 'published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
