=====
Usage
=====

To use Huey DRF API in a project, add it to your `INSTALLED_APPS`:

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
