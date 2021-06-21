from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.utils import timezone


def home(request):
    return render(request, "firstapp/home.html")

def about(request):
    return render(request, "firstapp/about.html")

def career(request):
    return render(request, "firstapp/career.html")

def os(request):
    return render(request, "firstapp/study/os.html")

def dc(request):
    return render(request, "firstapp/study/dc.html")

def curriculum(request):
    return render(request, "firstapp/study/curriculum.html")

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'firstapp/detail.html', {'post' : post})

def post(request):
    posts = Post.objects.all()
    return render(request, "firstapp/post.html", {'posts':posts})


def new(request):
    return render(request, 'firstapp/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('firstapp:detail',new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id =id)
    return render(request, 'firstapp/edit.html', {'post': edit_post})


def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title=request.POST['title']
    update_post.writer=request.user
    update_post.pub_date=timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('firstapp:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('firstapp:post')