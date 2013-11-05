from django.contrib import admin
from foo.models import Foo

class FooAdmin(admin.ModelAdmin):
    pass

admin.site.register(Foo, FooAdmin)