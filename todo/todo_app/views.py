from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddTaskForm
from .models import Task
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    if User.is_authenticated:
        tasks = Task.objects.filter(user_id= request.user.id)
        context = {
            "tasks":tasks
        }
        return render(request, "todo-tmp/index.html", context)
    else:
        return redirect("/accounts/login/")
def create_task(request):
    return render(request, "todo-tmp/create.html", {
        "action":"/save/",
        "inp_name":"",
        "inp_date":"",
    })

def save(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            modeeel = Task(name=request.POST['name'],date=request.POST['date'], user_id=request.user)
            modeeel.save()
            return redirect('/')
        # return HttpResponse("<h1>%s //// %s</h1>" %(request.POST["name"], form["date"]))
        return HttpResponse('<h1>invalid inputs</h1><a href="/create/">try again</a>')

def update(request, id):
    if request.method == "POST":
        task = Task.objects.get(id = id)
        task.name = request.POST["name"]
        task.date = request.POST["date"]
        task.save()
        return redirect("/")
    task = Task.objects.get(id = id)
    context = {
        "action":"",
        "inp_name":task.name,
        "inp_date":task.date.strftime(r"%Y-%m-%d"),
    }
    return render(request, "todo-tmp/create.html",context)

def delete(request,id):
    
    Task.objects.filter(id = id).delete()
    return redirect('/')
        



    