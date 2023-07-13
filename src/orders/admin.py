from django.contrib import admin
from . import models

admin.site.register(models.Cart)
admin.site.register(models.GoodInCart)
admin.site.register(models.Status)
admin.site.register(models.Order)
