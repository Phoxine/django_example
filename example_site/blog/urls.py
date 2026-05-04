from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    post_detail,
    post_list,
    optimized_post_list,
    optimized_post_detail,
    annotated_post_list,
    post_statistics,
    OptimizedPostListCreateView,
    OptimizedPostDetailView,
)

urlpatterns = [
    path('post/', post_list),
    path('post/<int:id>/', post_detail),
    path('post/optimized/', optimized_post_list),
    path('post/optimized/<int:id>/', optimized_post_detail),
    path('post/annotated/', annotated_post_list),
    path('post/statistics/', post_statistics),
    path('api/posts/', PostListCreateView.as_view()),
    path('api/posts/<int:pk>/', PostDetailView.as_view()),
    path('api/posts/optimized/', OptimizedPostListCreateView.as_view()),
    path('api/posts/optimized/<int:pk>/', OptimizedPostDetailView.as_view()),
]
