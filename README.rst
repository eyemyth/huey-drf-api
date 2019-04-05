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

The full documentation is at https://huey-drf-api.readthedocs.io.

Quickstart
----------

Install Huey DRF API::

    pip install huey-drf-api

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'hueydrfapi.apps.HueyDRFAPIConfig',
        ...
    )

Add Huey DRF API's URL patterns:

.. code-block:: python

    from hueydrfapi import urls as hueydrfapi_urls


    urlpatterns = [
        ...
        url(r'^', include(hueydrfapi_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

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
