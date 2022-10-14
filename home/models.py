from django.db import models


class DocInfos(models.Model):
    people = models.CharField(max_length=200)
    rotations = models.CharField(max_length=200)
    block = models.IntegerField()
    allYearResidents = models.CharField(max_length=200)
    partialYearResidents = models.CharField(max_length=200)
    mustDo = models.CharField(max_length=200)
    busyRotations = models.CharField(max_length=200)
    preference = models.CharField(max_length=200)
    impossibleAssignments = models.CharField(max_length=200)
    vacation = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)