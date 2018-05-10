from django.db import models


class Project(models.Model):
    name = models.TextField(default='No Name')
    description = models.TextField(default='')


class Epic(models.Model):
    name = models.TextField(default='No Name')
    description = models.TextField(default='')


class Task(models.Model):
    name = models.TextField(default='No Name')
    description = models.TextField(default='')
    epic = models.ForeignKey(Epic, on_delete=models.SET_NULL, null=True)


class SubTask(models.Model):
    name = models.TextField(default='No Name')
    description = models.TextField(default='')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
