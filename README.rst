django-multiemail-field
-----------------------

.. image:: https://travis-ci.org/sophilabs/django-multiemail-field.png?branch=master

Installation
============
.. code-block::

    pip install -e git+https://github.com/sophilabs/django-multiemail-field.git#egg=django-multiemail-field


Usage
=====
.. code-block::

    from django.db import models
    from multiemailfield import MultiEmailField

    class FooModel(models.Model):

        emails = MultiEmailField()

.. code-block::

    Textarea: +------------------------------------------------------------------------+
              | "User One" <userone@sophilabs.com>, User Two <usertwo@sophilabs.com>   |
              | User Three <userthree@sophilabs.com>                                   |
              +------------------------------------------------------------------------+
    
    Field value: [
        ('User One', 'userone@sophilabs.com'),
        ('User Two', 'usertwo@sophilabs.com'),
        ('User Three', 'userthree@sophilabs.com')
    ]

License
=======

django-multiemail-field is Copyright (c) 2017 sophilabs, inc. It is free software, and may be
redistributed under the terms specified in the `license <./LICENSE>`__ file.

About
=====

.. image:: https://s3.amazonaws.com/sophilabs-assets/logo/logo_300x66.gif
    :target: https://sophilabs.co

django-multiemail-field is maintained and funded by sophilabs, inc. The names and logos for
sophilabs are trademarks of sophilabs, inc.
