from django.db import models
from user.models import User

class Forum(models.Model):
    key_art = models.ImageField(
        upload_to='forum_images/',
        null=True,
        blank=True,
        default='forum/images/placeholder.svg'
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    popularity = models.BigIntegerField(default=0)
    description = models.TextField()

    def get_top_1_forum():
        return Forum.objects.order_by('-popularity').first()

    def get_top_5_forums():
        return Forum.objects.order_by('-popularity')[:5]

    def get_top_100_forums():
        return Forum.objects.order_by('-popularity')[:100]
    
    def get_all_forums_sorted_by_popularity():
        return Forum.objects.order_by('-popularity')

    def get_all_forums_sorted_by_name():
        return Forum.objects.order_by('name')
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comments/', null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Mention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} mentioned in comment {self.comment.id}'