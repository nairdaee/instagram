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

