from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Task
from datetime import date

'''
the below code is being done for the authentication purpose
'''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username, password = password)
        login(request, user)
        return redirect('task_list')
    
    return render(request, 'todo/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('task_list')
    
    return render(request, 'todo/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

'''this the completion of the code for the login and authentication
⚠️ REAL PROBLEMS YOU WILL FACE
Forgetting login_required
Forgetting user=request.user
Tasks leaking across users
'''
@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user).order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if not due_date: # if the due date is empty
            due_date = None # this is done so that the due date is not stored as a string
        Task.objects.create(title=title, due_date=due_date, user = request.user)
    return redirect('task_list')

@login_required   
def complete_task(request, task_id):
    task = Task.objects.get(id = task_id,user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id = task_id,user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
    return render(request, 'todo/delete_list.html', {'task': task})
    
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id = task_id,user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if not due_date:
            due_date = None
        task.due_date = due_date
        task.save()
        return redirect('task_list')
    
    return render(request, 'todo/edit_task.html', {'task': task})

@login_required
def toggle(request, task_id):
    task = Task.objects.get(id = task_id,user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def filter(request):
    
    if request.method == 'GET':
        filter= request.GET.get('type')
        if filter == 'completed':
            tasks = Task.objects.filter(user=request.user, completed = True)

        elif filter == 'incompleted':
            tasks = Task.objects.filter(user=request.user, completed = False)

        else:
            tasks = Task.objects.filter(user=request.user)

    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def mark_all(request):
    if request.method == 'POST':
        task = Task.objects.filter(user=request.user).update(completed = True)

        '''
        task = Task.objects.all()
        for i in task:
            i.completed = True
            i.save
        this was my initial thinking
        '''
    return redirect('task_list')

@login_required
def overdue(request):
    today = date.today()
    tasks = Task.objects.filter(user=request.user, due_date__lt = today, completed = False)

    return render(request, 'todo/task_list.html', {'tasks': tasks})

'''
__lt → less than  
__gt → greater than  
__lte → less than equal  
__gte → greater than equal  
'''



def events(request):
    # This is a simple example - you would typically fetch events from your database or an API
    events = [
        {"id": 1, "title": "Event 1", "date": "2024-07-01"},
        {"id": 2, "title": "Event 2", "date": "2024-07-02"},
        {"id": 3, "title": "Event 3", "date": "2024-07-03"},
        {"id": 4, "title": "Event 4", "date": "2024-07-04"},
        {"id": 5, "title": "Event 5", "date": "2024-07-05"},
        {"id": 6, "title": "Event 6", "date": "2024-07-06"},
        {"id": 7, "title": "Event 7", "date": "2024-07-07"},
        {"id": 8, "title": "Event 8", "date": "2024-07-08"},
        {"id": 9, "title": "Event 9", "date": "2024-07-09"},
        {"id": 10, "title": "Event 10", "date": "2024-07-10"},
    ]
    return JsonResponse(events, safe=False)