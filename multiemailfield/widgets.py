from django import forms
from multiemailfield import utils


class MultiEmailWidget(forms.Textarea):

    def render(self, name, value, attrs=None):
        value = utils.dump(value) or ''
        return super(MultiEmailWidget, self).render(name, value, attrs)