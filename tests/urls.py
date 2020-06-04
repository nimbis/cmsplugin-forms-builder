from django.conf.urls import include, url
import forms_builder.forms.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^forms/', include(forms_builder.forms.urls)),
]
