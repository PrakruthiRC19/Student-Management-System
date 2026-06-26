from django.urls import path 
from . import views

urlpatterns = [
    path('',views.display_student_view, name='display'),
    path('create/',views.create_student_view,name='create'),
    path('update/<int:student_id>',views.update_student_view,name='update'),
    path('delete/<int:student_id>',views.delete_student_view,name='delete'),
]