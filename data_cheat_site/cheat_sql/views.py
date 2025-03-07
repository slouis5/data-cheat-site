from django.shortcuts import render
from django.conf import settings

from .models import Chapter, Lesson, Clause, Image
import markdown, os
# Create your views here.

# test view
from django.http import HttpResponse


def index(request):

    # Query all chapters
    chapters = Chapter.objects.all().order_by("chapter_number")

    # Create a list of tuples, each containing a chapter and its related lessons
    chapter_lessons = [(chapter, Lesson.objects.filter(chapter=chapter).order_by("lesson_number")) for chapter in chapters]

    # Pass the list to the context
    context = {
        "chapter_lessons": chapter_lessons,
    }
    return render(request, "cheat_sql/base.html", context)

def chapter_ui(request, slug):
    
    # Query the chapter with the slug
    chapter = Chapter.objects.get(slug=slug)

    # Query all lessons related to the chapter
    lessons = Lesson.objects.filter(chapter=chapter).order_by("lesson_number")

    # Create a list of tuples, each containing a lesson and its related clauses
    #lesson_clauses = [(lesson, Clause.objects.filter(lesson=lesson)) for lesson in lessons]

    # Pass the list to the context
    context = {
        "chapter": chapter,
        "lessons": lessons,
    }
    return render(request, "cheat_sql/chapter.html", context)


def lesson_ui(request, slug, slug2):

    chapter = Chapter.objects.get(slug=slug)
    lesson = Lesson.objects.filter(chapter=chapter).get(slug=slug2)

    file_path = os.path.join(settings.MEDIA_ROOT, lesson.text_content.name)

    # Read the file content
    with open(file_path, 'r') as file:
        md_content = markdown.markdown(file.read())

    context = {
        "lesson": lesson,
        "md_content": md_content
    }
    return render(request, "cheat_sql/lesson_ui.html", context)
    

