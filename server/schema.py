import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug
from tasks.models import Task, SubTask, Epic, Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class EpicType(DjangoObjectType):
    class Meta:
        model = Epic

class TaskType(DjangoObjectType):
    epic = EpicType

    class Meta:
        model = Task

class SubTaskType(DjangoObjectType):
    task = Task
    
    class Meta:
        model = SubTask

class Query(graphene.ObjectType):
    all_epics = graphene.List(EpicType)
    all_tasks = graphene.List(TaskType)
    all_subtasks = graphene.List(SubTaskType)

    # Debug field (rawSql, parameters etc).
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_epics(self, info):
        return Epic.objects.all()

    def resolve_all_tasks(self, info):
        return Task.objects.select_related('epic').all()

    def resolve_all_subtasks(self, info):
        return SubTask.objects.select_related('task').all()

schema = graphene.Schema(query=Query)