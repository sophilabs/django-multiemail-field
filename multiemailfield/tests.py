from django.db import models
from django.test import TestCase

from . import MultiEmailField


class TestModel(models.Model):
    emails = MultiEmailField()


#class TestForm(forms.Form):
#    tz = TimeZoneFormField()
#    tz_opt = TimeZoneFormField(required=False)


#class TestModelForm(forms.ModelForm):
#    class Meta:
#        model = TestModel


class MultiEmailFieldTestCase(TestCase):

    def test_valid_creation(self):
        mc = TestModel.objects.create(emails="pablo ricco <pricco@gmail.com>")
        md = TestModel.objects.get(pk=mc.pk)
        print md
        print mc
