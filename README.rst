=============================
Huey DRF API
=============================

.. image:: https://badge.fury.io/py/huey-drf-api.svg
    :target: https://badge.fury.io/py/huey-drf-api

.. image:: https://travis-ci.org/eyemyth/huey-drf-api.svg?branch=master
    :target: https://travis-ci.org/eyemyth/huey-drf-api

.. image:: https://codecov.io/gh/eyemyth/huey-drf-api/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eyemyth/huey-drf-api

A DRF API for Huey

Documentation
-------------

The full documentation is at https://huey-drf-api.readthedocs.io. (Except it isn't, not yet.)

Quickstart
----------

Install Huey DRF API::

    pip install huey-drf-api

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'hueydrfapi',
        ...
    )

Add Huey DRF API's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path('', include('hueydrfapi.urls', namespace='hueydrfapi')),
        ...
    ]

Ensure that you have caching set up for Django.

Install `Huey <https://huey.readthedocs.io/en/latest/>`_. This package requires Huey >= 2.0. I recommend using Redis for Huey's queue and results store, as this is the easiest way to ensure there's one source of truth for the main Django process and Huey's consumer.

Install `Django Rest Framework <https://www.django-rest-framework.org>_`. So far I've only tested on the latest DRF (3.9). It should work with lower versions, but I'll confirm all of that when I have tests to run.

You can now create task groups and view them in the API. For example:

.. code-block:: python
from django.shortcuts import redirect
from hueydrfapi import TaskGroup
from myapp.tasks import my_task

def run_a_bunch_of_tasks(iterable):
   task_group = TaskGroup()
   for item in iterable:
      task_group.add(my_task(item))
   return redirect(task_group.url)

Features
--------

* TODO

Running Tests
-------------

* TODO: write tests

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
