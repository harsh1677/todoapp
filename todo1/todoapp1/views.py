from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todotable

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login') 
def todoappview(request):
    user_email = request.user.email
    #all_todo_items=todotable.objects.all()
    all_todo_items = todotable.objects.filter(user=user_email)
    return render(request, 'todolist.html', {'all_items':all_todo_items})

@login_required(login_url='/login')
def addtodo(request):
    user_email = request.user.email
    new_item=todotable()
    new_item.user = user_email
    new_item.content=request.POST.get('content')
    new_item.type=request.POST.get('type_cont')
    new_item.save()
    return HttpResponseRedirect('/todo/')

@login_required(login_url='/login')
def deleteTodoView(request, i):
    y = todotable.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 


