from django.db import models


# Create your models here.

class Routine(models.Model):
    DAYS_OF_WEEK = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.day} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} {self.subject}"


class Teacher(models.Model):
    Name = models.CharField(max_length=300)
    Sub = models.CharField(max_length=300)
    Contact = models.BigIntegerField()

    def __str__(self):
        return self.Name


class Class(models.Model):
    Classroom = models.IntegerField()
    Faculty = models.CharField(max_length=200)
    Sem = models.IntegerField()

    def __int__(self):
        return self.Classroom
    

class StudentCount(models.Model):
    StudentNo = models.IntegerField()

    def __int__(self):
        return self.StudentNo
    
class TeacherCount(models.Model):
    TeacherNo = models.IntegerField()

    def __int__(self):
        return self.TeacherNo
    
class RoomCount(models.Model):
    RoomNo = models.IntegerField()

    def __int__(self):
        return self.RoomNo