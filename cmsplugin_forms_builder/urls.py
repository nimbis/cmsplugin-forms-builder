from django.conf.urls import *

urlpatterns = patterns(
    "cmsplugin_forms_builder.views",
    url(r"(?P<slug>.*)/sent/$",
        "form_sent",
        name="form_sent"),
)
