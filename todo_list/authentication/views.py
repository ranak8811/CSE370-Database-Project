from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from authentication.forms import TeamForm
from .models import Team, Task


def handlelogin(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            request.session['email'] = user.username
            messages.success(request, 'Sucessfully logged in')
            """if user.first_name == 'admin':
                return redirect('/admin_dash')"""
            return redirect(all_tasks)

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/')
   return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Sucessfully logged out')
    return redirect('/')# Create your views here.


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repeat = request.POST['repeat']
        if repeat == password:
            user = User.objects.create_user(username=email, password=password, first_name= firstname, last_name=lastname)
            return redirect('/')
        else:
            return redirect('/signup')

    return render(request, 'signup.html')

def all_tasks(request):
    todos = Task.objects.all()
    print(type(todos[0].id))
    return render(request, 'all_task.html', {'todos': todos})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        Task.objects.create(task_name=task_name, category=category, priority=priority)
        return redirect('all_tasks')
def delete_todo(request,id):
    print(type(id))
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.delete()
    return render(request, 'all_task.html', {'todos': todos})
def change_status_pending(request,id):
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.status=False
    todo.save()
    return render(request, 'all_task.html', {'todos': todos})
def change_status_completed(request,id):
    todos = Task.objects.all()
    todo = Task.objects.get(id=id)
    todo.status=True
    todo.save()
    return render(request, 'all_task.html', {'todos': todos})

# SELECT * FROM Task WHERE priority = 'weekly';
def weekly_task(request):
    weekly_tasks = Task.objects.filter(priority__icontains='weekly')
    return render(request, 'weekly.html', {'weekly_tasks': weekly_tasks})

# SELECT * FROM Task WHERE priority = 'monthly';
def monthly_task(request):
    monthly_tasks = Task.objects.filter(priority__icontains='monthly')
    return render(request, 'monthly.html', {'monthly_tasks': monthly_tasks})

def completed_tasks(request):
    completed_tasks = Task.objects.filter(status=False)
    return render(request, 'completed.html', {'completed_tasks': completed_tasks})
def user_profile(request):
    user = request.user
    task_count = Task.objects.filter(user=user).count()
    return render(request, 'testPlanIt/templates/testPlanIt/user.html', {'task_count': task_count})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.members.add(request.user)
            return redirect('group_detail', pk=group.pk)
    
    else:
        form = TeamForm()
    return render(request, 'team.html', {'form':form})

def team(request):
    return render(request, 'team.html')

def team_detail(request, pk):
    group = Team.objects.get(pk=pk)
    return render(request, 'teamdash.html', {'group': group})

def join_team(request, pk):
    group = Team.objects.get(pk=pk)
    group.members.add(request.user)
    return redirect('group_detail', pk=pk)

def user_profile(request):
    user_groups = request.user.groups.all()
    return render(request, 'user.html', {'user_groups': user_groups})

def user(request):
    return render(request, 'user.html')

def teamdash(request):
    return render(request, 'teamdash.html')

def index(request):
    return render(request, 'index.html')