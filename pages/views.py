from django.shortcuts import render

def homepage(request):
    return render(request, 'pages/homepage.html')

def acerca(request):
    return render(request, 'pages/acerca.html')