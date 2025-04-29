from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    # Return follow lists
    def get_followees(self):
        return User.objects.filter(followers__follower=self).order_by('-followers__date_added')

    
    def get_followers(self):
        return User.objects.filter(followees__followee=self).order_by('-followees__date_added')
    
    def get_liked_posts(self):
        Post = apps.get_model('forum', 'Post')
        return Post.objects.filter(likes=self).order_by('-created_at')

    def get_my_posts(self):
        return self.post_set.all().order_by('-created_at')

    def get_my_comments(self):
        return self.comment_set.all().order_by('-created_at')
    
    


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='followees', on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followee')  # Ensures a user can't follow the same user twice
