from django.db import models
from cms.models.pluginmodel import CMSPlugin
from forms_builder.forms.models import Form


class PluginForm(CMSPlugin):
    """
    TODO.
    """

    form = models.ForeignKey(Form)
