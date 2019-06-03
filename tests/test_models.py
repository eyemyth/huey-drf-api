#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_huey-drf-api
------------

Tests for `huey-drf-api` api module.
"""

from uuid import uuid1

from django.test import TestCase
from huey.contrib.djhuey import HUEY
from hueydrfapi.api import TaskGroup
from hueydrfapi.exceptions import TaskGroupDoesNotExist

from tests.tasks import add_one


class TestTaskGroup(TestCase):
    def setUp(self):
        self.group = TaskGroup()
        self.group.add(add_one(1))
        self.group.add(add_one(2))
        self.group.add(add_one(3))

    def test_retrieving_by_id(self):
        retrieved = TaskGroup(task_group_id=self.group.task_group_id)
        self.assertEqual(self.group, retrieved)

    def test_creating_with_iterable(self):
        new_group = TaskGroup([
            add_one(4),
            add_one(5),
            add_one(6),
        ])
        self.assertIsInstance(new_group, TaskGroup)

    def test_raises_taskgroupdoesnotexist(self):
        with self.assertRaises(TaskGroupDoesNotExist):
            TaskGroup(task_group_id=str(uuid1()))

    def test_contains_invalid_type(self):
        self.assertFalse('not a task' in self.group)

    def test_add_invalid_type(self):
        with self.assertRaises(AttributeError):
            self.group.add('this is not a task')

    def test_add_task(self):
        task = self.group.add(add_one(4))
        task = HUEY.deserialize_task(task)
        self.assertTrue(task in self.group)

    def test_group_contains_task(self):
        task = list(self.group)[0]
        self.assertTrue(task in self.group)

    def test_discard_task(self):
        task = list(self.group)[0]
        self.group.discard(task)
        self.assertTrue(task not in self.group)

    def tearDown(self):
        pass
