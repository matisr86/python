from mezzanine import template
register = template.Library()

@register.inclusion_tag("pages/admin/form_mails.html",
                        takes_context=True)
def form_mails(context):
    """
    A list of last sended messages
    """
    from mezzanine.forms.models import FieldEntry, FormEntry, Form
    
    context["get_absolute_url"] = Form.objects.all()
    context["field"] = FieldEntry.objects.all
    context["form"] = FormEntry.objects.order_by('-entry_time')[:10]
    return context


@register.filter
def split(str, splitter):
    return str.split(splitter)[2]
