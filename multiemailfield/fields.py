from django.db.models import fields
from django.utils import six
from django.db.models.fields.subclassing import Creator
from django.utils.translation import ugettext_lazy as _

from email.utils import getaddresses
from multiemailfield.forms import MultiEmailFormField


class MultiEmailField(fields.TextField):
    """ Store and load email addresses """

    description = _('Multiple email addresses')

    def _load(self, value):
        return getaddresses([value])

    def _dump(self, value):
        return ', '.join(['"{0}" <{1}>'.format(*a) for a in value])

    def to_python(self, value):
        if value is None:
            return None
        if isinstance(value, six.string_types):
            return self._load(value)
        return value

    def get_db_prep_value(self, value, *args, **kwargs):
        if self.null and value is None and not kwargs.get('force'):
            return None
        return self._dump(value)

    def value_to_string(self, obj):
        return self.get_db_prep_value(self._get_val_from_obj(obj))

    def value_from_object(self, obj):
        return self._dump(super(MultiEmailField, self).value_from_object(obj))

    def formfield(self, **kwargs):
        defaults = {
            'form_class': kwargs.get('form_class', MultiEmailFormField),
        }
        defaults.update(kwargs)
        return super(MultiEmailField, self).formfield(**defaults)

    def contribute_to_class(self, cls, name):
        super(MultiEmailField, self).contribute_to_class(cls, name)
        setattr(cls, name, Creator(self))


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^multiemailfield\.fields\.(MultiEmailField)"])
except ImportError:
    pass