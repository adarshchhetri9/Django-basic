from django.db import models

# Create your models here.


class Llst(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class item(models.Model):
    llst = models.ForeignKey(Llst, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    cmpl = models.BooleanField()

    def __str__(self):
        return self.text
