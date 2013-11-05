from django import forms
from foo.models import Foo


class FooForm(forms.ModelForm):

    class Meta:
        model = Foo