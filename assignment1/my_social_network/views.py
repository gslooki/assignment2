from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from my_social_network.models import Userlink


def homepage(request):
    return HttpResponse("Home is where the heart is.")
def users(request):
    users = []
    for obj in User.objects.all():
      users.append(obj)
      users.append(" ")
    return HttpResponse(users)

def username(request, username):
    return HttpResponse(username)
def usernamefollowing(request, username):
    return HttpResponse(Userlink.objects.get(Userlink.objects.from_user.get(username)))
def usernamefollowers(request,username):
    return HttpResponse(Userlink.objects.get(Userlink.objects.to_user.get(username)))