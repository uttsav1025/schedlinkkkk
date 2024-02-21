from collections import defaultdict

from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User


class Base(View):
    views = {}


class HomePageView(Base):
    def get(self, request):
        return render(request, "landing.html", self.views)


def signup(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["confirm-password"]

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "The email is already used")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,

                )
                data.save()
                return redirect('/account/login/')
        else:
            messages.error(request, "The passwords do not match")
            return redirect('/signup')
    return render(request, 'signup.html')


class AdminLandingView(Base):
    def get(self, request):
        self.views['TeacherNumbers'] = TeacherCount.objects.all()
        self.views['StudentNumbers'] = StudentCount.objects.all()
        self.views['RoomNumbers'] = RoomCount.objects.all()

        return render(request, "admin_landing.html", self.views)


class AdminRoomView(Base):
    def get(self, request):
        self.views['classrooms'] = Class.objects.all()

        return render(request, "admin_rooms.html", self.views)





class AdminRoutineView(Base):
    def get(self, request):
        routines = Routine.objects.all().order_by('start_time', 'day')
        schedule = []

        time_slots = sorted(set([routine.start_time for routine in routines]))
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for time_slot in time_slots:
            row = {'Time': time_slot}
            for day in days:
                subjects = [routine.subject for routine in routines if
                            routine.day == day and routine.start_time == time_slot]
                row[day] = ", ".join(subjects)
            schedule.append(row)

        self.views['schedule'] = schedule
        return render(request, "admin_routines.html", self.views)


class AdminTeacherView(Base):
    def get(self, request):
        self.views['teachers'] = Teacher.objects.all()

        return render(request, "admin_teachers.html", self.views)
    

    
