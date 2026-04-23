from django.db import models
from datetime import date
from django.contrib.auth.models import User  ## for login purpose 


class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateField(null = True , blank = True)

    def __str__(self):
        return self.title