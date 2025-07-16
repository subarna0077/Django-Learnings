from django.shortcuts import render
from django.http import HttpResponseNotFound

blogs = {
    1: {
        'title': 'Getting Started with Django',
        'slug': 'getting-started-with-django',
        'image': 'https://picsum.photos/seed/django/600/400',
        'description': 'A beginner-friendly guide to building your first Django project from scratch.'
    },
    2: {
        'title': 'Understanding Django Templates',
        'slug': 'understanding-django-templates',
        'image': 'https://picsum.photos/seed/templates/600/400',
        'description': 'Learn how Django uses templates to dynamically generate HTML with reusable blocks.'
    },
    3: {
        'title': 'Django vs. Flask: Which to Choose?',
        'slug': 'django-vs-flask',
        'image': 'https://picsum.photos/seed/flask/600/400',
        'description': 'A comparison between Django and Flask to help you decide which framework fits your project.'
    }
}


# Create your views here.

def index(request):
    return render(request,'blog/home.html')

def allPosts(request):
    return render(request, 'blog/posts.html', {"blogs": blogs.values()})

def singlePost(request, slug):
    selected_blog = None
    for blog in blogs.values():
        if blog['slug']== slug:
            selected_blog = blog
            break

    if not selected_blog:
        return HttpResponseNotFound("No blog found")

    return render(request, 'blog/previewposts.html', {'blog': selected_blog})