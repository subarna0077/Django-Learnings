from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponseRedirect
from .models import Blog
from django.contrib import messages

# Create your views here.
def blogs(request):
    allBlog = Blog.objects.all()
    print(allBlog)
    return render(request, 'blog/blogs.html', {
        'blogs': allBlog
    })

def singleBlog(request, id):
    singleBlog = Blog.objects.get(id=id)
    print(singleBlog)
    return render(request, 'blog/singleblog.html', {
        'blog': singleBlog
    })


def admin(request):
    if(request.method == 'POST'):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog created successfully')
            return HttpResponseRedirect('/thank_you')  
    else:
        form = BlogForm()
    return render(request, 'blog/admin.html', {
        'form': form
    })

def thank_you(request):
    return render(request, 'blog/thank_you.html')