from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)

    def  __str__(self):
        return self.title

class Note_Detail(models.Model):
    description = models.TextField(max_length=1000)

    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.description