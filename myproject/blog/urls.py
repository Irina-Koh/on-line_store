from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)


app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blogpost_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blogpost_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blogpost_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blogpost_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blogpost_delete'),
]
