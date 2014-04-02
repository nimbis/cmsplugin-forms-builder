from cmsplugin_forms_builder.models import PluginForm
from forms_builder.forms.models import Form
from cms.test_utils.testcases import CMSTestCase


class FormTestCase(CMSTestCase):
    """
        Simple CRUD test for cmsplugin-forms-builder.
    """

    def setUp(self):
        # Create plugin
        form = Form.objects.create(
            title="Test Form",
            slug="testform",
            )

        self.plugin = PluginForm()
        self.plugin.form = form
        self.plugin.save()

    def test_plugin(self):

        # Read plugin
        self.assertEquals(self.plugin.form.title, "Test Form")
        self.assertEquals(self.plugin.form.slug, "testform")

        # Update plugin
        form = Form.objects.create(
            title="New Form",
            slug="newform",
            )

        self.plugin.form = form
        self.plugin.save()

        self.assertEquals(self.plugin.form.title, "New Form")
        self.assertEquals(self.plugin.form.slug, "newform")

        # Delete plugin
        self.plugin.delete()
        self.plugin = PluginForm.objects.first()

        self.assertEquals(self.plugin, None)
