from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Courses, Descriptions, Comments
from ..log_reg.models import Users

# Create your views here.
def index(request):
    if "current_user" not in request.session:
        return redirect("log_reg:index")

    context = {
        "courses": Courses.objects.all()
    }

    return render(request, "course_app/index.html", context)

def add_course(request):
    course = Courses.objects.create(course_name=request.POST["name"])
    Descriptions.objects.create(description=request.POST["desc"], course = course)

    return redirect("course_app:index")

def comment(request, id):

    if "current_user" not in request.session:
        return redirect("log_reg:index")

    course = Courses.objects.get(id=id)

    context = {
    "id": id,
    "comments": Comments.objects.filter(course=course),
    "course": course
    }

    return render(request, "course_app/comment.html", context)

def add_comment(request, id):

    if "current_user" not in request.session:
        return redirect("log_reg:index")

    Comments.objects.create(comment=request.POST["comment"], course=Courses.objects.get(id=id))

    return HttpResponseRedirect(reverse("course_app:comment", args=(id)))

def confirm_remove(request, id):

    if "current_user" not in request.session:
        return redirect("log_reg:index")

    context = {
    "id": id,
    "course": Courses.objects.get(id=id)
    }

    return render(request, "course_app/confirm_remove.html", context)

def remove(request, id):

    Courses.objects.get(id=id).delete()

    return redirect("course_app:index")

def user_courses(request):

    if "current_user" not in request.session:
        return redirect("log_reg:index")

    context = {
    "users" : Users.objects.all(),
    "courses" : Courses.objects.annotate(num_users=Count("user")),
    }

    return render(request, "course_app/users_courses.html", context)

def add_user_to_course(request):

    if "current_user" not in request.session:
        return redirect("log_reg:index")

    user = Users.objects.get(id=request.POST["user_id"])
    course = Courses.objects.get(id=request.POST["course_id"])
    course.user.add(user)

    return redirect("course_app:user_courses")
