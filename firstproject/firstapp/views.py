from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.utils import timezone

def home(request):
    return render(request, "firstapp/home.html")

def about(request):
    posts = Post.objects.all()
    return render(request, "firstapp/about.html", {'posts':posts})

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
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'firstapp/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)
