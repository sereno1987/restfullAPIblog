from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True)
    last_name=models.CharField(max_length=30, null=True, blank=True)
    avatar=models.ImageField(upload_to='./images', null=True, blank=True)

    def __str__(self):
       return str(self.name)+" "+str(self.last_name)

class Post(models.Model):
    title=models.CharField(max_length=50, null=False)
    description=models.CharField(max_length=500, null=False)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
       return str(self.title)+" --"+str(self.author)

