from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def contact(request):
    return render(request, 'main/contact.html')

def cv(request):
    return render(request, 'main/cv.html')