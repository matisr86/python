# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.encoding import python_2_unicode_compatible

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, SiteRelated
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to
from mezzanine.forms.models import Form
from fields import ColorField


class Color(models.Model):
    code = ColorField(_(u"Color"), default="6d6d6d",
        help_text=_('Color HEX code. Click on input to display Color picker.'))

    class Meta:
        abstract = True

    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^project\.fields\.ColorField"])


class Banner(Orderable):
    '''
    Banner connected to a Form
    '''

    homepage = models.ForeignKey(
        Form, verbose_name=_(u"Banner"), related_name="banner")
    bg = FileField(verbose_name=_(u"Background_img"),
        upload_to=upload_to("project.GalleryHome.image", "HomePage/background_img"),
        format="Image", max_length=255, null=True, blank=True)
    about_heading = models.CharField(_(u"Banner heading"),
        max_length=200, blank=True, null=True)
    about_desc = RichTextField(_(u"Banner description"), null=True, blank=True)


    class Meta:
        verbose_name = _(u"Banner Details")
        verbose_name_plural = _(u"Banner Details")


@python_2_unicode_compatible
class BannerImg(Orderable):
    '''
    BannerImg connected to a HomePage
    '''
    homepage = models.ForeignKey(
        Form, verbose_name=_(u"Banner images"), related_name="banner_img")
    img = FileField(verbose_name=_(u"Img"),
        upload_to=upload_to("project.GalleryHome.image", "HomePage/banner_img"),
        format="Image", max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = _(u"Banner images")
        verbose_name_plural = _(u"Banner images")


    def __str__(self):
        return unicode(self.img.filename)

    def image_name(self):
        name = _(u'None')
        if self.img:
            name = self.img.filename
        return name

    image_name.allow_tags = True
    image_name.short_description = _(u"Image name")

    def date(self):
        date = _(u'None')
        if self.img:
			date = self.img.datetime
        return date

    date.allow_tags = True
    date.short_description = _(u"Date")


@python_2_unicode_compatible
class WhatWeDo(Orderable):
    '''
    WhatWeDoing connected to a HomePage
    '''
    homepage = models.ForeignKey(
        Form, verbose_name=_(u"What we do"), related_name="what_do")
    img = FileField(verbose_name=_(u"Img"),
        upload_to=upload_to("project.GalleryHome.image", "HomePage/what_we_do_img"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(_(u"Main title"),
        max_length=200, blank=True, null=True)
    description = RichTextField(_(u"Description"))


    class Meta:
        verbose_name = _(u"What we do")
        verbose_name_plural = _(u"What we do")

    def __str__(self):
        return unicode(self.img.filename)

    def image_name(self):
        name = _(u'None')
        if self.img:
            name = self.img.filename
        return name

    image_name.allow_tags = True
    image_name.short_description = _(u"Image name")

    def date(self):
        date = _(u'None')
        if self.img:
			date = self.img.datetime
        return date

    date.allow_tags = True
    date.short_description = _(u"Date")


@python_2_unicode_compatible
class Realisations(Orderable):
    '''
    Realisations connected to a HomePage
    '''
    homepage = models.ForeignKey(
        Form, verbose_name=_(u"Realisations"), related_name="realisations")
    img = FileField(verbose_name=_(u"Img"),
        upload_to=upload_to("project.GalleryHome.image", "HomePage/realisations_img"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(_(u"Main title"),
        max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = _(u"Realisation")
        verbose_name_plural = _(u"Realisations")

    def __str__(self):
        return unicode(self.img.filename)

    def image_name(self):
        name = _(u'None')
        if self.img:
            name = self.img.filename
        return name

    image_name.allow_tags = True
    image_name.short_description = _(u"Image name")

    def date(self):
        date = _(u'None')
        if self.img:
			date = self.img.datetime
        return date

    date.allow_tags = True
    date.short_description = _(u"Date")


@python_2_unicode_compatible
class About(Orderable):
    '''
    About connected to a HomePage
    '''
    homepage = models.ForeignKey(
        Form, verbose_name=_(u"About"), related_name="about")
    main_title = RichTextField(_(u"Main description"))
    img = FileField(verbose_name=_(u"Img"),
        upload_to=upload_to("project.GalleryHome.image", "HomePage/about_img"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(_(u"Title"),
        max_length=200, blank=True, null=True)
    description = RichTextField(_(u"Description"))

    class Meta:
        verbose_name = _(u"About")
        verbose_name_plural = _(u"About")

    def __str__(self):
        return unicode(self.img.filename)

    def image_name(self):
        name = _(u'None')
        if self.img:
            name = self.img.filename
        return name

    image_name.allow_tags = True
    image_name.short_description = _(u"Image name")

    def date(self):
        date = _(u'None')
        if self.img:
			date = self.img.datetime
        return date

    date.allow_tags = True
    date.short_description = _(u"Date")


class FooterContent(Orderable):
    '''
    A footer content
    '''

    homepage = models.ForeignKey(
        Form, verbose_name=_(u"Footer"), related_name="footer")
    adress_content = RichTextField(_(u"Adress content"))
	
    img = FileField(verbose_name=_(u"Map"),
        upload_to=upload_to("project.GalleryHome.image",
                            "HomePage/google_map"),
        format="Image", max_length=255, null=True, blank=True)
    
    copyright = RichTextField(_(u"Copyright"))

    class Meta:
        verbose_name = _(u"Footer")
        verbose_name_plural = _(u"Footer")


'''
Column choices for social media
'''
COLUMNS_CHOICES_SOCIAL_MEDIA = (
    ('0', '----'),
    ('1', 'Facebook'),
    ('2', 'Twiteer'),
    ('3', 'Pinterest'),
    ('4', 'Instagram'),
)


class SocialMedia(Orderable):
    '''
    A social media in footer content
    '''
    footercontent = models.ForeignKey(Form,
        verbose_name=_(u"Socials"), related_name="socials")
    columns = models.CharField(_(u"Columns"),
        max_length=1, choices=COLUMNS_CHOICES_SOCIAL_MEDIA, default='0',
        help_text=_(u"Social media columns"))
    link = models.URLField(_(u"Link"), max_length=2000, null=True, blank=True,
        help_text=_(u"Optional link for social media"))
    footer_social = models.BooleanField(_(u"Display social media in footer"),
        default=True)
    header_social = models.BooleanField(_(u"Display social media in header"),
        default=True)

    class Meta:
        verbose_name = _(u"Social Media")
        verbose_name_plural = _(u"Social Media")
