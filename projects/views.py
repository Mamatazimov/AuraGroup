from django.shortcuts import render
from django.views import View

from .models import Projects, Images



class ProjectListView(View):
    def get(self, request):
        projects = Projects.objects.all()
        for project in projects:
            print(project)
        return render(request, 'projects/project_list.html', {})





