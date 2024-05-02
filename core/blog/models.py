from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        "accounts.Profile", on_delete=models.CASCADE, related_name="post"
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ManyToManyField("blog.Category", related_name="cat_post")
    banner = models.ImageField()
    body = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
