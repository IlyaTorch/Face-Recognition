from django.contrib import admin
from .models import Url, BoundingBox

# Register your models here.
admin.site.register(Url)
admin.site.register(BoundingBox)
