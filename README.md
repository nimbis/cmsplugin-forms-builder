django-cms plugin for django-forms-builder
==========================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-forms-builder.svg?branch=master
   :target: https://travis-ci.org/nimbis/cmsplugin-forms-builder

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-forms-builder/badge.png?branch=master
   :target: https://coveralls.io/r/nimbis/cmsplugin-forms-builder?branch=master


This plugin provides a simple means of inserting django-forms-builder forms
as django-cms plugins.


Requires
--------

* django-cms >= 3.0
* django >= 1.5
* django-forms-builder >= 0.10


Setup
-----

* Run `pip install cmsplugin-forms-builder` or download this package and run `python setup.py install`

* Ensure 'django.contrib.messages', 'cms', 'forms_builder.forms',
  'cmsplugin_forms_builder' are in your project's INSTALLED_APPS.

* If you're using South execute `python manage.py migrate`, Otherwise run
  `python manage.py syncdb` within your project directory.


History
-------

0.1.11:

    * Update to Django 1.7 migrations

0.1.4:

	* Fixed bug on Safari browser, make sure that 'cmsplugin_forms_builder' comes
	  above 'forms_builder.forms' in INSTALLED_APPS.

0.1.1:

    * Fixed bugs related to imports in views.py

0.1.0:

    * Initial commit.
