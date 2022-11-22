from django.contrib import admin
from django.urls import path
from apps.core.views import *
from apps.blog.views import *
from apps.cart.views import *
from apps.newsletter.views import *
from apps.order.views import *
from apps.store.views import *
from apps.userprofile.views import *
from django.conf.urls.static import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
