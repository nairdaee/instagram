from .models import Image, Comments, Followers, Profile
from django import forms
from django.forms import ModelForm

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'userId', 'user']

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','images', 'description']

class Likes(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','description','comments','date','user','userId','profile','image','name','caption']

class FollowForm(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','follower']