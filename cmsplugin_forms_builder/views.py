from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import Site
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.http import urlquote
from email_extras.utils import send_mail_template

from forms_builder.forms.forms import FormForForm
from forms_builder.forms.models import Form
from forms_builder.forms.signals import form_invalid, form_valid
from forms_builder.forms.utils import split_choices


def form_sent(request, slug, template="forms/form_sent.html"):
    """
    Show the response message.
    """
    published = Form.objects.published(for_user=request.user)
    form = get_object_or_404(published, slug=slug)
    context = {"form": form}
    if request.META.get('HTTP_REFERER'):
        request.session['form_sent'] = True
        messages.add_message(
            request,
            messages.SUCCESS,
            "The form has been submitted successfully.")
        return redirect(request.META.get('HTTP_REFERER'))
    return render_to_response(template, context, RequestContext(request))
