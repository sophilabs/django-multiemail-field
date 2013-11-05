django-multiemail-field
-----------------------

.. image:: https://travis-ci.org/sophilabs/django-multiemail-field.png?branch=master

Installation
============
.. code-block::

    pip install -e git+git@github.com:sophilabs/django-multiemailfield.git#egg=django-multiemailfield


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
