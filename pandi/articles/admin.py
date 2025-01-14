from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published', 'slug')
    list_filter = ('is_published', 'published', 'author')
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ('-published',)
    fields = (
        'title', 'slug', 'author', 'content', 
        'is_published', 'published',
    )
    readonly_fields = ('published',)

