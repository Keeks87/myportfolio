from django.shortcuts import render

# Create your views here.

def blog_list(request):
    """View function to display a list of blog posts."""
    return render(request, 'blog/blog_list.html')

def blog_detail(request):
    """View function to display a single blog post."""
    return render(request, 'blog/blog_detail.html')

def blog_create(request):
    """View function to create a new blog post."""
    return render(request, 'blog/blog_create.html')

def blog_edit(request):
    """View function to edit an existing blog post."""
    return render(request, 'blog/blog_edit.html')
