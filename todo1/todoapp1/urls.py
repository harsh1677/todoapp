from django.urls import path
from . import views
app_name='todoapp1'

urlpatterns = [
    path('',views.index, name='index'),
    path('todo/', views.todoappview, name='todo' ),
    path('addtodo/',views.addtodo,),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView)
]