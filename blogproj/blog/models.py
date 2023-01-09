from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField
from django.utils import timezone
from django.urls import reverse

from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    picture = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        self.likes.count()
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def get_comments(cls, id):
        comments = cls.objects.filter(post__id=id)
        return comments

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-pk"]
class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)






