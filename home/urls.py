from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='landing'),
    path('signup/', signup, name='signup'),
    path('admin_landing/', AdminLandingView.as_view(), name='adminl'),
    path('admin_teachers/', AdminTeacherView.as_view(), name='admint'),
    path('admin_routine/', AdminRoutineView.as_view(), name='adminr'),
    path('admin_rooms/', AdminRoomView.as_view(), name='adminrm'),

]