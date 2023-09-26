from django.shortcuts import render
from .models import skills, project


# Create your views here.
def index(request):
    skill = skills.objects.all()
    projects = project.objects.all()
    return render(request, 'index.html', {'skill':skill, 'projects':projects})

