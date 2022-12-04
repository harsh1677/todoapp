from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todotable
# Create your views here.

def index(request):
    return render(request, 'index.html')
 
def todoappview(request):
    all_todo_items=todotable.objects.all()
    return render(request, 'todolist.html', {'all_items':all_todo_items})

def addtodo(request):
    new_item=todotable()
    new_item.content=request.POST.get('content')
    new_item.type=request.POST.get('type_cont')
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodoView(request, i):
    y = todotable.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 


