# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Realisations.description'
        db.delete_column(u'project_realisations', 'description')

        # Deleting field 'Realisations.description_en'
        db.delete_column(u'project_realisations', 'description_en')

        # Deleting field 'Realisations.description_pl'
        db.delete_column(u'project_realisations', 'description_pl')


        # Changing field 'Realisations.title'
        db.alter_column(u'project_realisations', 'title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Realisations.title_en'
        db.alter_column(u'project_realisations', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Realisations.title_pl'
        db.alter_column(u'project_realisations', 'title_pl', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    def backwards(self, orm):
        # Adding field 'Realisations.description'
        db.add_column(u'project_realisations', 'description',
                      self.gf('mezzanine.core.fields.RichTextField')(default=1),
                      keep_default=False)

        # Adding field 'Realisations.description_en'
        db.add_column(u'project_realisations', 'description_en',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Realisations.description_pl'
        db.add_column(u'project_realisations', 'description_pl',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Realisations.title'
        db.alter_column(u'project_realisations', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Realisations.title_en'
        db.alter_column(u'project_realisations', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Realisations.title_pl'
        db.alter_column(u'project_realisations', 'title_pl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'forms.form': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Form', '_ormbases': [u'pages.Page']},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'button_text_en': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'button_text_pl': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_message_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email_message_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_subject_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email_subject_pl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'response': ('mezzanine.core.fields.RichTextField', [], {}),
            'response_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'response_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_meta_title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_meta_title_pl': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '()', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'slug_pl': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'project.about': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'About'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            'description_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'about'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'main_title': ('mezzanine.core.fields.RichTextField', [], {}),
            'main_title_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'main_title_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'project.banner': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Banner'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'about_desc': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'about_desc_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'about_desc_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'about_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'about_heading_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'about_heading_pl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'bg': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'project.bannerimg': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'BannerImg'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_img'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'project.footercontent': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'FooterContent'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adress_content': ('mezzanine.core.fields.RichTextField', [], {}),
            'adress_content_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'adress_content_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'copyright': ('mezzanine.core.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'footer'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'project.realisations': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Realisations'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realisations'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'project.socialmedia': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'SocialMedia'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'columns': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'footer_social': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'footercontent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'socials'", 'to': u"orm['forms.Form']"}),
            'header_social': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'})
        },
        u'project.whatwedo': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'WhatWeDo'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            'description_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pl': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'what_do'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['project']