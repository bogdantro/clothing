from django.contrib import admin
from django.urls import path
from apps.core.views import *
from apps.cart.views import *
from apps.order.views import *
from apps.store.views import *
from apps.userprofile.views import *
from django.conf.urls.static import *
from apps.store.api import *
from apps.cart.webhook import *
from apps.userprofile.views import *
from apps.order.views import admin_order_pdf
from django.contrib.auth import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    path('admin-stellcare/', admin.site.urls),
    path('admin-stellcare/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

    path('', home, name='home'),

    #AUTH
    path('logg-in/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('lag-bruker/', signup, name='signup'),
    path('min-bruker/', myaccount, name='myaccount'),
    path('logg-ut/', views.LogoutView.as_view(), name='logout'),




    #API
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/add_to_cart_bundle/', api_add_to_cart_bundle, name='api_add_to_cart_bundle'),
    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),



    #STORE
    path('sok/', search, name='search'),
    path('handlekurv/', cart_detail, name='cart-detail'),
    path('handlekurv/order-success/', success, name='success'),
    path('stellcare-checkout/', checkout, name='checkout'),
    path('hooks/', webhook, name='webhook'),
    path('produkt/:<slug>/', product_detail, name='product_detail'),
    path('category/:<slug>/', category, name='category'),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
