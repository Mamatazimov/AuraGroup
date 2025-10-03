from django.shortcuts import render
from django.views import View

from .models import Member




class MembersListView(View):
    def get(self, request):

        members = Member.objects.all()
        for member in members:
            print(member)

        return render(request, 'members/member_list.html', {})
