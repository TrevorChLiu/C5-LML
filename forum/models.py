from django.db import models

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