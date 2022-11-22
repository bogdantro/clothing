from django.contrib import admin
from .models import FAQ, Coupon


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created_at']
    search_fields = ['question']

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Coupon)
