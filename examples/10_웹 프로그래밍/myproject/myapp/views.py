from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
