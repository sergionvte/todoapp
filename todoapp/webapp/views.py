from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(request):

    logged = False

    if logged:
        values = {
            'logged': logged,
            'name': 'Sergio',
            'todos': [
                'Task 1',
                'Task 2',
                'Task 3',
                'Task 4',
                'Task 5',
                'Task 6',
                'Task 7',
                'Task 8',
                'Task 9 ',
                'Task 10',
            ]
        }
    else:
        values = {'logged': logged}

    return render(request, 'index.html', values)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})
