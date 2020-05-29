from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    '''
    image Class for all images added to the app
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userId=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-post_date']
    
    def save_image(self):
        '''
        Method to save new images
        '''
        self.save()
    
    def delete_image(self):
        '''
        Method to delete images
        '''
        self.delete()
    
    @classmethod
    def all_images(cls):
        '''
        Method to view all images
        '''
        images = cls.objects.all()
        return images
    @classmethod
    def search_by_users(cls,term):
        result=cls.objects.filter(user__username__icontains=term)
        return result

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()

    def __str__(self):
        return self.comment
    
    def save_comments(self):
        self.save()

class Followers(models.Model):
    user = models.CharField(max_length=20, default="")
    follower = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.follower
    
    def save_followers(self):
        self.save()

class PhotoLikes(models.Model):
    postid = models.IntegerField()
    liker = models.CharField(max_length=20)

    def __str__(self):
        return self.liker
    
    def save_likes(self):
        self.save()


class Profile(models.Model):
    pic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=30)
    userId=models.IntegerField()


    def __str__(self):
        return self.bio

    class Meta:
        ordering=['pic']

    def save_profile(self):
        self.save()

    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile
    