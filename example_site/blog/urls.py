from django.urls import path
from .views import PostListCreateView, PostDetailView, post_detail, post_list

urlpatterns = [
    path('post/', post_list),
    path('post/<int:id>/', post_detail),
    path('api/posts/', PostListCreateView.as_view()),
    path('api/posts/<int:pk>/', PostDetailView.as_view()),
]
