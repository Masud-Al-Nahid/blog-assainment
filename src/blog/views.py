from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home_view(request):
    blog = Blog.objects.all().first()
    #pagination
    queryset = Post.objects.filter(post_status='published')
    per_page = 5
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    #featured_post
    featured_one = Post.objects.filter(featured_post=True)[:1].get()
    featured_two = Post.objects.filter(featured_post=True)[1:2].get()
    featured_three = Post.objects.filter(featured_post=True)[2:3].get()

    
    context = {
        'posts': posts,
        'blog': blog,
        'featured_one': featured_one,
        'featured_two': featured_two,
        'featured_three': featured_three,

    }
    template_name = 'blog/garden-index.html'
    return render(request, template_name , context)

def category_view(request, slug):
    queryset = category.objects.filter(slug=slug).all()
    template_name = 'blog/garden-category.html'
    context = { 'queryset': queryset }
    return render(request, template_name, context)

def single_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    blog_info = Blog.objects.all().first()
    template_name = 'blog/garden-single.html'
    context = { 'post': post, 'blog_info': blog_info }
    return render(request, template_name, context)
    