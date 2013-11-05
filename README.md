Django Multiple Email Field
    
    pip install -e git+git@github.com:sophilabs/django-multiemailfield.git#egg=django-multiemailfield


    Textarea: +------------------------------------------------------------------------+
              | '"User One" <userone@sophilabs.com>, User Two <usertwo@sophilabs.com>  |
              | User Three <userthree@sophilabs.com>'                                  |
              +------------------------------------------------------------------------+
    
    Field value: [
        ('User One', 'userone@sophilabs.com'),
        ('User Two', 'usertwo@sophilabs.com'),
        ('User Three', 'userthree@sophilabs.com')
    ]
