from django.db import models

# Create your models here.
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    app_names = [app.split(".")[0] for app in settings.INSTALLED_APPS if not app.startswith("django")]
    APPS_LIST = list(zip(app_names, app_names))
    app_name = models.CharField(max_length=50, choices=APPS_LIST,default=app_names[0])
    #syllabus = models.TextField()
    #logo = models.ImageField()
    def __str__(self):
        return self.name
    
class Contributor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    #bio = models.TextField()
    #avatar = models.ImageField()
    email = models.EmailField()
    def __str__(self):
        return self.name
