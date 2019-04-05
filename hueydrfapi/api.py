# -*- coding: utf-8 -*-
from collections.abc import MutableSet
from django.core.cache import cache
from huey.contrib.djhuey import HUEY
from uuid import uuid1
from pickle import PickleError

from .exceptions import TaskGroupDoesNotExist


class TaskGroup(MutableSet):
    '''
    elements is a set of serialized huey tasks
    self.add serializes, so we add the tasks themselves

    we expose the tasks themselves via __iter__
    '''

    def __init__(self, iterable=[], task_group_id=None):
        self.task_group_id = task_group_id

        if not self.task_group_id:
            self.task_group_id = str(uuid1())
            self.elements = set()
            for value in iterable:
                self.add(value)
            cache.set(self.task_group_id, self.elements)
        else:
            try:
                self.elements = set(cache.get(task_group_id))
            except TypeError:
                raise TaskGroupDoesNotExist

    def __iter__(self):
        return iter([HUEY.deserialize_task(task) for task in self.elements])

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return str(list(self.__iter__()))

    def add(self, item):
        try:
            task = HUEY.serialize_task(item.task)
            if task not in self.elements:
                self.elements.add(task)
            cache.set(self.task_group_id, self.elements)
        except PickleError:
            raise

    def discard(self, item):
        try:
            self.elements.remove(item)
        except ValueError:
            pass
