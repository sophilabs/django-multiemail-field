from django.db.models import fields
from django.db.models.fields.subclassing import Creator
from django.utils.translation import ugettext_lazy as _
from multiemailfield.forms import MultiEmailFormField
from multiemailfield import utils


class MultiEmailField(fields.TextField):
    """ Store and load email addresses """

    description = _('Multiple email addresses')

    def to_python(self, value):
        return utils.load(value)

    def get_db_prep_value(self, value, *args, **kwargs):
        if self.null and value is None and not kwargs.get('force'):
            return None
        return utils.dump(value)

    def value_to_string(self, obj):
        return self.get_db_prep_value(self._get_val_from_obj(obj))

    def value_from_object(self, obj):
        return utils.dump(super(MultiEmailField, self).value_from_object(obj))

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
    add_introspection_rules([], ["^multiemailfield\.fields\.MultiEmailField"])
except ImportError:
    pass
