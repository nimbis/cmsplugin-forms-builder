from django.db import models
from cms.models.pluginmodel import CMSPlugin
from forms_builder.forms.models import Form


class PluginForm(CMSPlugin):
    """
        Model for the plugin form.
    """

    form = models.ForeignKey(Form, on_delete=models.CASCADE,)

    def __str__(self):
        return self.form.title
