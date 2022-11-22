from django.shortcuts import render

# Create your views here.


def subscriber(request):
    return render(request, 'core/bli-medlem.html') 
