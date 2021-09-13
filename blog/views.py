from django.shortcuts import render, get_object_or_404
from blog.models import Post, BlogCategory
# Create your views here.


def index(request):
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_list(request):
    posts = Post.published.all()
    categories = BlogCategory.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)
