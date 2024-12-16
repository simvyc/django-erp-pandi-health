from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'published_date', 'is_published']
        read_only_fields = ['id', 'slug', 'published_date', 'author']  # Make slug read-only
