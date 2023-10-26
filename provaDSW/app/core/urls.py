from django.urls import path
from .views import *

urlpatterns = [
    path('list_student/', ListStudent.as_view(), name='list_student'),
    path('create_student/', CreateStudent.as_view(), name='create_student'),
    path('edit_student/<int:pk>/', EditStudent.as_view(), name='edit_student'),
    path('delete_student/<int:pk>/', DeleteStudent.as_view(), name='delete_student'),
    path('student_detail/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]