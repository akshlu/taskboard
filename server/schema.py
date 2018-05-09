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
    epics = graphene.List(EpicType)
    tasks = graphene.List(TaskType)
    subtasks = graphene.List(SubTaskType)
    projects = graphene.List(ProjectType)

    # Debug field (rawSql, parameters etc).
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_projects(self, info):
        return Project.objects.all()

    def resolve_epics(self, info):
        return Epic.objects.all()

    def resolve_tasks(self, info):
        return Task.objects.select_related('epic').all()

    def resolve_subtasks(self, info):
        return SubTask.objects.select_related('task').all()

schema = graphene.Schema(query=Query)