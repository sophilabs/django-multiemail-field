from django import forms
from multiemailfield.widgets import MultiEmailWidget
from multiemailfield import utils


class MultiEmailFormField(forms.CharField):

    def __init__(self, *args, **kwargs):
        if 'widget' not in kwargs:
            kwargs['widget'] = MultiEmailWidget
        super(MultiEmailFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return utils.load(super(MultiEmailFormField, self).clean(value))
