django-cms plugin for django-forms-builder
==========================================

This plugin provides a simple means of inserting django-forms-builder forms
as django-cms plugins.


Requires
----------------

* django-cms >= 2.4
* django >= 1.5
* django-forms-builder >= 0.10


Setup
-----

* Run `pip install cmsplugin-forms-builder` or download this package and run `python setup.py install`

* Ensure 'django.contrib.messages', 'cms', 'forms_builder.forms',
  'cmsplugin_forms_builder' is in your project's INSTALLED_APPS.

* If you're using South execute `python manage.py migrate`, Otherwise run
  `python manage.py syncdb` within your project directory.


History
-------

0.1.1:
    * Fixed bugs related to imports in views.py

0.1.0:
    * Initial commit.