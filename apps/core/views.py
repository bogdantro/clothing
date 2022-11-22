import json
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.store.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from django.conf import settings
from apps.cart.cart import Cart
from apps.order.models import Order
from .forms import ContactForm, HelpForm
from django.core.mail import send_mail, BadHeaderError
from .models import FAQ
from django.views.decorators.csrf import csrf_exempt



def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    featuredPr = Product.objects.filter(is_featured=True)
    featuredCat = Category.objects.filter(is_home_page=True)   
    cart = Cart(request)    

    for product in featuredPr:
        if cart.has_product(product.id):
            product.in_cart = True
        else:
            product.in_cart = False    


    context = {
        'featuredPr':featuredPr,
        'products':products,
        'category':category,
        'featuredCat':featuredCat,
     }
     
    return render(request, 'core/home.html', context)


def order_confirmation(request):
    order = Order.objects.get(pk=id)
    return render(request, 'core/order_confirmation.html', {'order':order})


#KUNDESERVICE
def kundeservice(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            fra = form.cleaned_data['fra']
            grunn = form.cleaned_data['grunn']
            beskjed = form.cleaned_data['beskjed']
            try:
                send_mail(fra, grunn, beskjed, ['support@stellcare.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pages/contact/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')    

def faq(request):
    faq = FAQ.objects.all()

    context = {
        'faq':faq,
    }

    return render(request, 'pages/contact/redirections/faq.html', context) 

def refunds(request):

    return render(request, 'pages/contact/redirections/refunds.html')    

def tjenester(request):

    return render(request, 'pages/contact/redirections/tjenester.html')    

def dine_bestilinger(request):

    return render(request, 'pages/contact/redirections/dine-bestilinger.html')    

def kundefordeler(request):

    return render(request, 'pages/contact/redirections/kundefordeler.html')

def jobber(request):

    return render(request, 'pages/contact/redirections/jobs.html')  

def pakesporing(request):

    return render(request, 'pages/contact/redirections/pakesporing.html') 

def terms(request):

    return render(request, 'pages/contact/redirections/terms.html') 
                      
###############################################################################################


#HELP ME
def hjelp_meg(request):
    featuredPr = Product.objects.filter(is_featured=True)

    if request.method == 'GET':
        form = HelpForm()
    else:
        form = HelpForm(request.POST)
        if form.is_valid():
            hud_type = form.cleaned_data['hud_type']
            fra_epost = form.cleaned_data['fra_epost']
            alder = form.cleaned_data['alder']
            kjønn = form.cleaned_data['kjønn']
            try:
                send_mail(hud_type, alder, fra_epost, kjønn['support@stellcare.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pages/help/help-me.html", {'form': form, 'featuredPr':featuredPr})
          
###############################################################################################

def om(request):
    return render(request, 'pages/about/about.html')

@csrf_exempt
def search(request):
    query = request.GET.get('q','')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(name__icontains=query))|(Q(description__icontains=query))
            #I assume "text" is a field in your model
            #i.e., text = model.TextField()
            #Use | if searching multiple fields, i.e., 
            #queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
            results = Product.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'core/search.html', {'results':results, 'query':query})

    #You can also set context = {'results':results, 'query':query} after 
    #the else: (same indentation as return statement), and 
    #use render(request, 'home.html', context) if you prefer. 
  


