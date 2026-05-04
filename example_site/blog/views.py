from django.shortcuts import render
from rest_framework import generics
from django.db.models import Count, Avg
from .models import Post
from .serializers import PostSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Optimized views using select_related and prefetch_related
def optimized_post_list(request):
    posts = Post.objects.select_related('author').prefetch_related('comments').all()
    return render(request, 'blog/optimized_post_list.html', {'posts': posts})

def optimized_post_detail(request, id):
    post = Post.objects.select_related('author').prefetch_related('comments').get(id=id)
    return render(request, 'blog/optimized_post_detail.html', {'post': post})


class OptimizedPostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related('author').prefetch_related('comments').all().order_by('-created_at')
    serializer_class = PostSerializer


class OptimizedPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related('author').prefetch_related('comments').all()
    serializer_class = PostSerializer


# Views demonstrating annotate and aggregate
def annotated_post_list(request):
    posts = Post.objects.annotate(num_comments=Count('comments')).all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_statistics(request):
    average_rating = Post.objects.aggregate(Avg('rating'))['rating__avg']
    total_posts = Post.objects.count()
    return render(request, 'blog/statistics.html', {'average_rating': average_rating, 'total_posts': total_posts})
