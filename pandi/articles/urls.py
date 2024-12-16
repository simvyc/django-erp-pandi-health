from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView
from .views import article_list

urlpatterns = [
    # path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    # path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('', article_list, name='article_list'),
]
