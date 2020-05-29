from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comments, Followers, PhotoLikes

@login_required(login_url='/accounts/login/')
def home(request):
    current_user=request.user.id
    images = Image.all_images()
    profile_image=Profile.objects.filter(id=current_user)
    profile=profile_image.reverse()[0:1]
    comments=Comments.objects.all()
    users=User.objects.all().exclude(id=request.user.id)
    row = round(len(images)/4)
    return render(request, 'home.html', {"images": images,"profile":profile,"users":users,"comments":comments})
