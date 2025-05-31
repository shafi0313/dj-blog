from django.urls import path
from .views import PostCreateView, PostListView  # PostListView পূর্বে তৈরি করা লাগবে

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),             # → /posts/
    path('create/', PostCreateView.as_view(), name='create'),  # → /posts/create/
]