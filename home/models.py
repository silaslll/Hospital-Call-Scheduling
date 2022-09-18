from django.db import models


class DocInfos(models.Model):
    input1 = models.CharField(max_length=200)
    input2 = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)