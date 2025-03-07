from django.db import models
from django.utils.text import slugify
import random

# Create your models here.


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200, unique=True)
    chapter_number = models.IntegerField(default=10000)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    COURSES = [
        ("sql", "SQL"),
        ("python", "Python"),
        ]
    course = models.CharField(
        max_length=20,
        choices=COURSES,
        default="sql",
    )
    # chapter_number = models.IntegerField(primary_key=True)
    chapter_description = models.TextField()
    published = models.BooleanField(default=False)
    chapter_date = models.DateTimeField("date published")

    def __str__(self):
        return self.chapter_name
    
    def nb_ch(self):
        return Chapter.objects.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.chapter_name)
        #Check if the chapter_number already exists for another object
        if Chapter.objects.filter(chapter_number=self.chapter_number).exists():
            # Increment chapter_number of all chapters with chapter_number greater than or equal to the current chapter's chapter_number
            Chapter.objects.filter(chapter_number__gte=self.chapter_number).exclude(id=self.id).update(chapter_number=models.F('chapter_number') + 1)
        super().save(*args, **kwargs)


class Clause(models.Model):
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    clause_name = models.CharField(max_length=200)
    VARIANTS = [
        ("gernaral_sql", "General SQL"),
        ("pl_sql", "PL/SQL"),
        ("transact_sql", "Transact-SQL"),
        ("mysql", "MySQL"),
        ("postgresql", "PostgreSQL"),
        ("mssql", "MS SQL Server"),
        ("oracle", "Oracle"),
    ]
    DBS = [
        ("mysql", "MySQL"),
        ("postgresql", "PostgreSQL"),
        ("mssql", "MS SQL Server"),
        ("oracle", "Oracle"),
        ("all", "All"),
    ]
    db = models.CharField(
        max_length=20,
        choices=DBS,
        default="all",
    )
    variant = models.CharField(
        max_length=20,
        choices=VARIANTS,
        default="gernaral_sql",
    )
    clause_description = models.TextField()

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lessons_image/')


class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=200)
    lesson_number = models.IntegerField(default=10000)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    LESSON_TYPES = [
        ("lab", "Lab"),
        ("lecture", "Lecture"),
        ("quiz", "Quiz"),
    ]
    lesson_type = models.CharField(
        max_length=20,
        choices=LESSON_TYPES,
        default="lecture",
    )
    lesson_clauses = models.ManyToManyField(Clause,blank=True)
    LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    level = models.CharField(
        max_length=20,
        choices=LEVELS,
        default="beginner",
    )
    lesson_description = models.TextField()
    text_content  = models.FileField(upload_to='lessons_text/', blank=True)
    images = models.ManyToManyField(Image)
    published = models.BooleanField(default=False)
    lesson_date = models.DateTimeField("date published")

    def __str__(self):
        return self.lesson_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.lesson_name)
        #Check if the lesson_number already exists for another object
        if Lesson.objects.filter(lesson_number=self.lesson_number).exists():
            # Increment lesson_number of all chapters with lesson_number greater than or equal to the current chapter's lesson_number
            Lesson.objects.filter(lesson_number__gte=self.lesson_number).exclude(id=self.id).update(lesson_number=models.F('lesson_number') + 1)
        super().save(*args, **kwargs)
