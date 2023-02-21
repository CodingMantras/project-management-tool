from django.shortcuts import render
from project.models import Project
from tasks.models import Task
from teams.models import Team


def admindashboard(request):
    # Retrieve all projects, tasks and teams
    projects = Project.objects.all()
    tasks = Task.objects.all()
    teams = Team.objects.all()

    # Pass the data to the template
    context = {
        'projects': projects,
        'tasks': tasks,
        'teams': teams,
    }
    return render(request, 'admindashboard.html', context)
