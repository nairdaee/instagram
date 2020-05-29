from django.contrib import admin
from .models import Image, Profile, Followers, Comments

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Followers)
admin.site.register(Comments)
