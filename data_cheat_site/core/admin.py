from django.contrib import admin

# Register your models here.
from .models import Course, Contributor

admin.site.register(Course)
admin.site.register(Contributor)