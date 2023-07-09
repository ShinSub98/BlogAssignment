from django.db import models
from members.models import CustomUser

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=100)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True, null=True)
    


class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE, default="")
    created_at = models.DateField(auto_now_add=True, null=True)
    comment = models.TextField(default="")

    def __str__(self):
        return self.comment
