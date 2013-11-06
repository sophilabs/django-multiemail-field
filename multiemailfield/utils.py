from email.utils import getaddresses
from django.utils import six


def load(value):
    if not value:
        return None
    if isinstance(value, six.string_types):
        return getaddresses([value.strip()])
    else:
        return value


def dump(value):
    if not value:
        return None
    if isinstance(value, list):
        return ', '.join(['"{0}" <{1}>'.format(*a) for a in value])
    else:
        return value
