from django.http import Http404
from django.utils.module_loading import autodiscover_modules

from rest_framework import viewsets
from rest_framework.response import Response
from huey.contrib.djhuey import HUEY

from .api import TaskGroup
from .serializers import TaskGroupSerializer
from .exceptions import TaskGroupDoesNotExist

autodiscover_modules('tasks')


class TaskGroupViewSet(viewsets.ViewSet):
    basename = 'taskgroup'
    lookup_field = 'task_group_id'

    def retrieve(self, request, task_group_id=None):
        print(HUEY._registry.__dict__)
        try:
            task_group = TaskGroup(task_group_id=task_group_id)
        except TaskGroupDoesNotExist:
            raise Http404

        serializer = TaskGroupSerializer(task_group)
        return Response(serializer.data)
