from django.shortcuts import render

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