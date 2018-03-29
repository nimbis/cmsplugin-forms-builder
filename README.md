# cmsplugin-forms-builder

![Screenshot](https://raw.githubusercontent.com/nimbis/cmsplugin-forms-builder/master/screenshots/readme.png)

![Screenshot2](https://raw.githubusercontent.com/nimbis/cmsplugin-forms-builder/master/screenshots/readme2.png)

### A [django-forms-builder](https://github.com/stephenmcd/django-forms-builder) plugin for [django-cms](https://github.com/divio/django-cms)

[![Build Status](https://travis-ci.org/nimbis/cmsplugin-forms-builder.svg?branch=master)](https://travis-ci.org/nimbis/cmsplugin-forms-builder)

This plugin provides a simple means of inserting django-forms-builder forms
as django-cms plugins. You will need to override django-forms-builder's default `built_form.html` [template](https://github.com/stephenmcd/django-forms-builder/blob/master/forms_builder/forms/templates/forms/includes/built_form.html) in your project in order to POST the form using AJAX, which is then handled appropriately by django-forms-builder's built in views. See the sample [template](https://github.com/nimbis/cmsplugin-forms-builder/blob/master/sample/templates/forms/includes/built_form.html) for a better idea of how this works.


## Requires

* django >= 1.8
* django-cms >= 3.3.1
* django-forms-builder


## Setup

* Verify django-cms and django-forms-builder are installed correctly.

* Run `pip install cmsplugin-forms-builder` or download this package and run `python setup.py install`

* Add `'forms_builder.forms', 'cmsplugin_forms_builder'` to your project's INSTALLED_APPS.

* In order to submit your django-forms-builder forms via AJAX, you will need to override django-forms-builder's default `built_form.html` template. Since everyone's use case is different, this repository does not come with a predefined template in order to work "out-of-the-box". However, a sample [template](https://github.com/nimbis/cmsplugin-forms-builder/blob/master/sample/templates/forms/includes/built_form.html) is provided to help you get started.

Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).


## History

v1.1.1 (March 29, 2018):

    * Organize the plugin in the admin UI with other form plugins.
    * Display a useful string description of forms in the admin UI.

v1.1.0 (September 8, 2016):

    * Adding migration required for Django CMS v3.3.1 and later, which is now
      required for this app.

v1.0.1:

    * Include README.md in the manifest.

v1.0.0:

    * Removed unnecessary code in views.py and urls.py.
    * Improved documentation in README
    * Added screenshots and sample `build_form.html` template
    * Fixed setup.py, no longer requires pip>=6.0
    * Loosened requirements slightly

v0.1.11:

    * Update to Django 1.7 migrations

v0.1.4:

	* Fixed bug on Safari browser, make sure that 'cmsplugin_forms_builder' comes
	  above 'forms_builder.forms' in INSTALLED_APPS

v0.1.1:

    * Fixed bugs related to imports in views.py

v0.1.0:

    * Initial commit
