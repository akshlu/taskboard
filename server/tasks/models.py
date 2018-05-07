from django.db import models


class Project(models.Model):
    name = models.TextField
    description = models.TextField


class Epic(models.Model):
    name = models.TextField
    description = models.TextField


class Task(models.Model):
    name = models.TextField
    description = models.TextField
    epic = models.ForeignKey(Epic, on_delete=models.SET_NULL, null=True)


class SubTask(models.Model):
    name = models.TextField
    description = models.TextField
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
