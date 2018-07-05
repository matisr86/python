# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from copy import deepcopy
from django.core.files.storage import FileSystemStorage

from mezzanine.conf import settings
from mezzanine.core.admin import TabularDynamicInlineAdmin, SingletonAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.galleries.models import Gallery
from mezzanine.generic.models import ThreadedComment
from mezzanine.core.admin import DisplayableAdmin
from mezzanine.pages.models import Link, RichTextPage
from mezzanine.pages.admin import PageAdmin
from mezzanine.forms.models import Form
from mezzanine.forms.admin import FieldAdmin, FormAdmin
from mezzanine.forms.models import Form, Field

from models import Banner
from models import SocialMedia
from models import FooterContent

from models import BannerImg, WhatWeDo, Realisations, About

fs = FileSystemStorage(location=settings.FORMS_UPLOAD_ROOT)


page_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
page_fieldsets[0][1]['fields'][1:0] = ['title_en', 'title_pl']
page_fieldsets[0][1]['fields'][5:0] = ['login_required']
page_fieldsets[0][1]['fields'].remove('title')
page_list_display = ['title_en', 'title_pl', 'status', 'login_required']

page_fieldsets[1][1]['fields'].remove(('description', 'gen_description'))
page_fieldsets[1][1]['fields'][1:0] = ['_meta_title_en', '_meta_title_pl']
page_fieldsets[1][1]['fields'][4:0] = ['slug_en', 'slug_pl', ('description_en',
                                        'description_pl', 'gen_description')]
page_fieldsets[1][1]['fields'].remove('_meta_title')


class PageAdminTranslated(PageAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(PageAdminTranslated,
        self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


class BannerImgInline(TabularDynamicInlineAdmin):
    model = BannerImg
    max_num = 10
    readonly_fields = ('image_name', 'date')
    fieldsets = [(None,
                    {'fields': ('img', 'image_name', 'date', '_order')})]
    classes = ('collapse-closed',)


class WhatWeDoInline(TabularDynamicInlineAdmin):
    model = WhatWeDo
    readonly_fields = ('image_name', 'date')
    fieldsets = [(None,
                    {'fields': ('title_en', 'title_pl', 'description_en', 'description_pl', 'img', 'image_name', 'date', '_order')})]
    classes = ('collapse-closed',)


class RealisationsInline(TabularDynamicInlineAdmin):
    model = Realisations
    readonly_fields = ('image_name', 'date')
    fieldsets = [(None,
                    {'fields': ('title_en', 'title_pl', 'img', 'image_name', 'date', '_order')})]
    classes = ('collapse-closed',)


class AboutInline(TabularDynamicInlineAdmin):
    model = About
    readonly_fields = ('image_name', 'date')
    fieldsets = [(None,
                    {'fields': ('main_title_en', 'main_title_pl', 'title_en', 'title_pl', 'description', 'img', 'image_name', 'date', '_order')})]
    classes = ('collapse-closed',)


class BannerInline(TabularDynamicInlineAdmin):
    model = Banner
    max_num = 2
    exclude = ('about_heading', 'about_desc')
    classes = ('collapse-closed',)


class SocialMediaInline(TabularDynamicInlineAdmin):
    model = SocialMedia
    classes = ('collapse-closed',)


class SocialMediaContentInline(TabularDynamicInlineAdmin):
    model = FooterContent
    max_num = 1
    exclude = ('adress_content',)
    classes = ('collapse-closed',)


class FieldInline(TabularDynamicInlineAdmin):
    model = Field
    exclude = ('label', 'choices', 'default', 'placeholder_text', 'help_text')
    classes = ('collapse-closed',)


class FormAdmin(FormAdmin):
    model = FormAdmin

    class Media:
        css = {'all': ('mezzanine/css/admin/form.css',)}
	
    form_fieldsets = deepcopy(page_fieldsets)
    field_fieldsets = deepcopy(FieldAdmin.fieldsets)
    form_fieldsets = list(form_fieldsets)
    form_fieldsets.insert(2,
        (_(u'Email description'),
            {'fields': (('button_text_en', 'button_text_pl'),
                        'response_en', 'response_pl'),
            'classes': ('collapse-closed',)})
    )
    form_fieldsets.insert(3,
        (_(u'Email'),
            {'fields': ('send_email',
                        'email_copies', ('email_subject_en',
                        'email_subject_pl'), ('email_message_en',
                        'email_message_pl')),
            'classes': ('collapse-closed',)})
    )

    fieldsets = form_fieldsets
    inlines = (FieldInline, BannerInline, BannerImgInline,
                WhatWeDoInline, RealisationsInline, AboutInline,
                SocialMediaContentInline, SocialMediaInline)


admin.site.unregister(Form)
admin.site.register(Form, FormAdmin)
admin.site.unregister(BlogPost)
admin.site.unregister(ThreadedComment)
admin.site.unregister(Link)
admin.site.unregister(RichTextPage)
admin.site.unregister(Gallery)
