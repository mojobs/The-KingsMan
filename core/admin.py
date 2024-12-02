from django.contrib import admin

from .models import Cloth, Customer, Delivery, Orders, Price

# Register your models here.
admin.site.register(Cloth)

admin.site.register(Customer)

admin.site.register(Delivery)

admin.site.register(Orders)

admin.site.register(Price)
