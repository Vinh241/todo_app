from django.db import models
from django.contrib.auth.models import User
class TodoApp(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    time = models.DateTimeField(null=True, blank=True)  
    author = models.ForeignKey(
        User,
        on_delete= models.CASCADE
    )
    def __str__(self) -> str:
        return self.title