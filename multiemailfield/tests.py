from django.db import models
from django.test import TestCase
from django.db import IntegrityError

from multiemailfield.fields import MultiEmailField


class TestModel(models.Model):
    emails = MultiEmailField()


class NullTestModel(models.Model):
    emails = MultiEmailField(null=True, blank=True)


class MultiEmailFieldTestCase(TestCase):

    def test_valid_email(self):
        mc = TestModel.objects.create(emails='pablo ricco <pricco@gmail.com>')
        self.assertListEqual(mc.emails, [('pablo ricco', 'pricco@gmail.com',)])
        md = TestModel.objects.get(pk=mc.pk)
        self.assertListEqual(md.emails, mc.emails)
        with self.assertRaises(IntegrityError):
            TestModel.objects.create(emails=None)

    def test_empty(self):
        mc = NullTestModel.objects.create(emails='')
        self.assertEqual(mc.emails, None)
        mc = NullTestModel.objects.create(emails=None)
        self.assertEqual(mc.emails, None)

    def test_multiple(self):
        emails = 'pablo ricco <pricco@gmail.com>\n' + \
                 '"pablo ricco" <pricco@gmail.com>,' + \
                 'pablo ricco <pricco@gmail.com'
        mc = TestModel.objects.create(emails=emails)
        self.assertListEqual(mc.emails, [('pablo ricco', 'pricco@gmail.com',),
                                         ('pablo ricco', 'pricco@gmail.com',),
                                         ('pablo ricco', 'pricco@gmail.com',)])
