from django.contrib import admin

# Register your models here.
from .models import People, Address, Doctor, Bio

# Register your models here.
admin.site.register(People)

admin.site.register(Address)

admin.site.register(Doctor)

admin.site.register(Bio)