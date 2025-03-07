from django.contrib import admin

from .models import Chapter, Clause, Lesson, Image
# Register your models here.
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(Clause)
admin.site.register(Image)
