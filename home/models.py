from django.db import models
from taggit.managers import TaggableManager

# Home Model
class Home(models.Model):
    name = models.CharField(max_length=50)
    authorImage = models.ImageField(upload_to='Author')
    authorExp = models.CharField(max_length=100)
    shortDesc = models.TextField(max_length=300)

    def __str__(self):
        return self.name  


# Blog Post Model
class Blogpost(models.Model):
    author = models.CharField(max_length=50)
    postTitle = models.CharField(max_length=500)
    thumPic = models.ImageField(upload_to='post')
    tags = TaggableManager()
    description = models.TextField()
    posttime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    read = models.IntegerField(default=0)

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
    
    class Meta:
        ordering = ['-pk']

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    email = models.CharField(max_length=150,default='')
    creation = models.DateTimeField(auto_now_add=True)
