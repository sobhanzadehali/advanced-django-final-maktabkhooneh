from django.db import models
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:30] + " . . ."