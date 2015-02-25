# cmsplugin-forms-builder


### A [django-forms-builder](https://github.com/stephenmcd/django-forms-builder) plugin for [django-cms](https://github.com/divio/django-cms)

[![Build Status](https://travis-ci.org/nimbis/cmsplugin-forms-builder.svg?branch=master)](https://travis-ci.org/nimbis/cmsplugin-forms-builder)

This plugin provides a simple means of inserting django-forms-builder forms
as django-cms plugins.


## Requires

* django-cms >= 3.0
* django >= 1.5
* django-forms-builder >= 0.10


## Setup

* Verify django-cms and django-forms-builder are installed correctly.

* Run `pip install cmsplugin-forms-builder` or download this package and run `python setup.py install`

* Add `'cmsplugin_forms_builder'` to your project's INSTALLED_APPS.

* If you're using Django < 1.7 in conjunction with South, make sure that your SOUTH_MIGRATION_MODULES setting contains `'cmsplugin_forms_builder': 'cmsplugin_forms_builder.south_migrations'`, like so:

```
SOUTH_MIGRATION_MODULES = {
    # your other south migration modules...
    'cmsplugin_forms_builder': 'cmsplugin_forms_builder.south_migrations',
}
```

## History

0.1.11:

    * Update to Django 1.7 migrations

0.1.4:

	* Fixed bug on Safari browser, make sure that 'cmsplugin_forms_builder' comes
	  above 'forms_builder.forms' in INSTALLED_APPS.

0.1.1:

    * Fixed bugs related to imports in views.py

0.1.0:

    * Initial commit.
