from .views import TeacherRudView, TeacherAPIView
from .views import StudentRudView, StudentAPIView
from django.urls import path

urlpatterns = [
    path('teacher/', TeacherAPIView.as_view(), name='teacher-post-createNPost'),
    path('teacher/<int:pk>', TeacherRudView.as_view(), name='teacher-post-rud'),

    path('student/', StudentAPIView.as_view(), name='student-post-createNPost'),
    path('student/<int:pk>', StudentRudView.as_view(), name='student-post-rud'),
    
]
