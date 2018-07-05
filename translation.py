# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from mezzanine.pages.models import Page
from mezzanine.forms.models import Form, Field
from models import Banner, WhatWeDo, Realisations
from models import About, FooterContent


class PageTitleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', '_meta_title', 'description')


class BannerTranslation(TranslationOptions):
    fields = ('about_heading', 'about_desc')


class WhatWeDoTranslation(TranslationOptions):
    fields = ('title', 'description')


class RealisationsTranslation(TranslationOptions):
    fields = ('title',)


class AboutTranslation(TranslationOptions):
    fields = ('main_title', 'title', 'description')


class FooterContentTranslation (TranslationOptions):
    fields = ('adress_content',)


class FormTranslation (TranslationOptions):
    fields = ('content', 'button_text', 'response',
        'email_subject', 'email_message',)


class FieldTranslation (TranslationOptions):
    fields = ('label', 'default', 'choices', 'placeholder_text', 'help_text',)


translator.register(Page, PageTitleTranslationOptions)
translator.register(Form, FormTranslation)
translator.register(Field, FieldTranslation)
translator.register(Banner, BannerTranslation)
translator.register(WhatWeDo, WhatWeDoTranslation)
translator.register(About, AboutTranslation)
translator.register(Realisations, RealisationsTranslation)
translator.register(FooterContent, FooterContentTranslation)
