from django.shortcuts import render, redirect
from .models import BlogPost

# Create your views here.


def index(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog_project/index.html', {'posts': posts})

def about_me(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog_project/about-me.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        date = request.POST.get('date')

        new_blog = BlogPost(
            title = title,
            description = description,
            image = image,
            date = date  
        )

        new_blog.save()
        return redirect('index')


    return render(request, 'blog_project/add-posts.html')


def continue_reading(request, blog_id):
    data = BlogPost.objects.get(id = blog_id)

    return render(request, 'blog_project/continue-reading.html', {'data': data})

def edit(request, blog_id):
    data = BlogPost.objects.get(id = blog_id)

    if request.method == 'POST':
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')
        data.date = request.POST.get('date')

        image = request.FILES.get('image')
        if image:
            data.image = image 

        data.save()
        return redirect('index')
        

    return render(request, 'blog_project/edit.html', {'data': data})


def delete(request, blog_id):
    data = BlogPost.objects.get(id = blog_id)

    data.delete()
    return redirect('index')