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

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    current_user_id=request.user.id
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.userId=current_user_id
            image.profile=current_user_id
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})

@login_required(login_url="/accounts/login/")
def myprofile(request):
    try:
        current_user=request.user.id
        profile_photos=Image.objects.filter(userId=current_user)
        profile_image=Profile.objects.filter(userId=current_user).all()
        profile=profile_image.reverse()[0:1]

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos,"pic":profile})

@login_required(login_url="/accounts/login/")
def edit(request):
    current_user_id=request.user.id
    profile=Profile.objects.filter(userId=current_user_id)
    if len(profile)<1:

        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.userId=current_user_id
                profile.save()
            return redirect("myprofile")
        else:
            form=EditProfile()
            return render(request,"edit.html",{"form":form})
    else:
        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES )
            if form.is_valid():
                profile=form.save(commit=False)
                bio=form.cleaned_data['bio']
                pic=form.cleaned_data['pic']
                update=Profile.objects.filter(userId=current_user_id).update(bio=bio,pic=pic)
                profile.userId=current_user_id
                profile.save(update)
            return redirect("profile")
        else:

            form=EditProfile()
            return render(request,"edit.html",{"form":form})


@login_required(login_url="/accounts/login/")
def comments(request,image_id):
    try:
        image=Image.objects.filter(id=image_id).all()
        comment=Comments.objects.filter(images=image_id).all()
    except Exception as e:
        raise  Http404()

    imag=Image.objects.filter(id=image_id).all()
    count=0
    for i in imag:
        count+=i.likes

    if request.method=='POST':
        form=Likes(request.POST)
        k=request.POST.get("like","")
        if k:
            if form.is_valid:
                likes=form.save(commit=False)
                current_user=request.user
                postid=image_id
                if not PhotoLikes.objects.filter(liker=current_user, postid=postid).exists():
                    Image.objects.filter(id=postid).update(likes=F('likes')+1)
                    like = PhotoLikes(postid=postid, liker=current_user)
                    like.save()
                else:
                    Image.objects.filter(id=postid).update(likes=F('likes')-1)
                    PhotoLikes.objects.filter(postid=postid, liker=current_user).delete()
                return redirect('comment',image_id)
    else:
        forms=Likes()
    if request.method=='POST':
        current_user=request.user
        i=request.POST.get("id","")
        form=CommentForm(request.POST)
        if form.is_valid:
            comments=form.save(commit=False)
            comments.user=current_user
            comments.images=i
            comments.save()
            return redirect('comment',image_id)
    else:
        form=CommentForm()
    return render(request,"comment.html",{"images":image,'form':form,"comments":comment,"count":count,"forms":forms})
