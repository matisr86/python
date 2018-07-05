from django import forms
from django.utils.safestring import mark_safe
from django.db.models import CharField
from django.conf import settings


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                '/static/css/project/colorpicker.css',
            )
        }

        js = (
            '/static/js/project/picker-csrf.js',
            '/static//js/jquery-1.11.1.min.js',
            '/static/js/project/colorpicker.js',
            
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, id, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(id, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').ColorPicker({
    onSubmit: function(hsb, hex, rgb, el) {
        $(el).val(hex);
        $(el).ColorPickerHide();
    },
    onBeforeShow: function () {
        $(this).ColorPickerSetColor(this.value);
    }
    })
    .bind('keyup', function(){
        $(this).ColorPickerSetColor(this.value);
    })

        </script>''' % id)


class ColorField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)
