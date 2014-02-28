from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import PluginForm
from django.utils.translation import ugettext_lazy as _
from forms_builder.forms.views import form_detail


class FormsPlugin(CMSPluginBase):
    model = PluginForm
    render_template = "forms/form_detail.html"

    def render(self, context, instance, placeholder):
        context['form'] = instance.form
        return context


plugin_pool.register_plugin(FormsPlugin)
