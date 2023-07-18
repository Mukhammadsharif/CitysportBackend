from django.contrib import admin
from .models import Order, Sauna, Pool, Billiard, Training, Subscription

admin.site.register(Order)
admin.site.register(Sauna)
admin.site.register(Pool)
admin.site.register(Billiard)
admin.site.register(Training)
admin.site.register(Subscription)
