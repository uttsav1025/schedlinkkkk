from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Routine)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(StudentCount)
admin.site.register(TeacherCount)

admin.site.register(RoomCount)

class Routine(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'subject')
    list_filter = ('day',)
    ordering = ('day', 'start_time')
