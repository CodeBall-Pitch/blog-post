from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20,blank=True,null=True)
    subtitle = models.CharField(max_length=20,blank=True,null=True)
    thumbnail = models.ImageField(blank=True,null=True)


    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000,blank=True,null=True)
    thumbnail = models.ImageField(blank=True,null=True) 
    status = models.CharField(max_length=10, choices=(('draft','Draft'),('published','Published')))
    categories = models.ManyToManyField(Category,blank=True,null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title