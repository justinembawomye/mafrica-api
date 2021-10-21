from django.urls import path
from .views import CoursesAPIView,CoursesListCreate

urlpatterns = [
     path('addcourse', CoursesAPIView.as_view(), name='add_course'),
     path('courses/',CoursesListCreate.as_view() ),
]