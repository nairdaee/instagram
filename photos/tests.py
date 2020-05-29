from django.test import TestCase
from .models import Image, Profile, Comments, Followers
import datetime as dt

class TestProfile(TestCase):
    def setUp(self):
        self.profile=Profile(pic="img.png",bio="Funlife",userId=1)
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_initialization(self):
        self.assertEqual(self.profile.pic,"img.png")
        self.assertEqual(self.profile.bio,"Funlife")
        self.assertEqual(self.profile.userId,1)

    def test_save(self):
        self.profile.save_profile()
        prof=Profile.objects.all()
        self.assertTrue(len(prof)>0)

    def test_delete(self):
        self.profile.delete_profile()
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)

class TestImage(TestCase):
    def setUp(self):
        self.comment=Comments(images=1,comment='this is dope')
        self.follow=Followers(user="profile",follower='like')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_instance_follow(self):
        self.assertTrue(isinstance(self.follow,Followers))

    def test_save(self):
        self.follow.save_followers()
        prof=Followers.objects.all()
        self.assertTrue(len(prof)>0)


