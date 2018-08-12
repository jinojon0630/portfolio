from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blogs': blogs})

def detail(request, b_id):
    blog = get_object_or_404(Blog, pk=b_id)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})