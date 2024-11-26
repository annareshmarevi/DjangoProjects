from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklist(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'tasks'

class Taskdetail(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'taskdetail'

class Taskupdate(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'tasku'
    fields = ('taskname','priority','date')
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})

class Taskdelete(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classhome')
# Create your views here.
def home(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(taskname=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'tasks':tasks})
def detail(request,taskid):
    task=Task.objects.get(id=taskid)
    return render(request,'detail.html',{'taskd':task})

def delete(request, taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})