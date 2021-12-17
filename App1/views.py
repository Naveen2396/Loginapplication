from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Tasklist #for App1.models import Tasklist
from App1.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def input(request):
    if(request.method=="POST"):
        form=TaskForm(request.POST or None)
        if(form.is_valid()):
            instance=form.save(commit=False)
            instance.owner=request.user
            instance.save()
        messages.success(request,("New Task Added"))
        return redirect('task') #here task is the url specified in urls.py
    else:
        all_tasks=Tasklist.objects.all()
        paginator=Paginator(all_tasks,10)  #creating object of paginator class
                                          #all_tasks--->on what objects pagination to be perform
                                          #s--->how many objects to show on each page
        page=request.GET.get('pg')   #To get a particular page,here within the get we can specify rename
                                     #i.e pg or page
                                     #Now reloading all_tasks as per our pagination results
        all_tasks=paginator.get_page(page)
        return render(request,'base.html',{'all_tasks':all_tasks})


def contact(request):
    context={
        'contact_text':'welcome to the contact page'
    }
    return render(request,'contact.html',context)

def aboutus(request):
    context={
        'aboutus_text':'welcome to the about us page'
    }
    return render(request,'about us.html',context)

def index(request):
    context={
             'index_text':'Welcome To The Index Page'
    }
    return render(request,'index.html',context)
@login_required
def delete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('task')
@login_required
def edit_task(request,task_id):
    if(request.method=="POST"):
     task=Tasklist.objects.get(pk=task_id)
     form=TaskForm(request.POST or None,instance=task)
     if(form.is_valid()):  #add here
         form.save()
     messages.success(request,("Task Edited..!!"))
     return redirect('task') #here task is the url specified in urls.py
    else:
        task_obj=Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
@login_required
def complete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('task')
@login_required
def pending_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('task')





