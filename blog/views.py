from django.shortcuts import render
from .models import Post, Author, Category
# Create your views here.
def home(request):
    categories=Category.objects.all()[0:3]
    featured=Post.objects.filter(featured=True)[0:3]
    latest=Post.objects.order_by('-timestamp')[0:3]
    context={
        'categories':categories,
        'featured':featured,
        'latest':latest
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)

def category_post(request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'cat.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_post.html', context)