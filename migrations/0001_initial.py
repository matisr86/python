# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'project_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banner', to=orm['forms.Form'])),
            ('bg', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('about_heading', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('about_desc', self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'project', ['Banner'])

        # Adding model 'BannerImg'
        db.create_table(u'project_bannerimg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banner_img', to=orm['forms.Form'])),
            ('img', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'project', ['BannerImg'])

        # Adding model 'WhatWeDo'
        db.create_table(u'project_whatwedo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='what_do', to=orm['forms.Form'])),
            ('img', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'project', ['WhatWeDo'])

        # Adding model 'Realisations'
        db.create_table(u'project_realisations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='realisations', to=orm['forms.Form'])),
            ('img', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'project', ['Realisations'])

        # Adding model 'About'
        db.create_table(u'project_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='about', to=orm['forms.Form'])),
            ('main_title', self.gf('mezzanine.core.fields.RichTextField')()),
            ('img', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'project', ['About'])

        # Adding model 'FooterContent'
        db.create_table(u'project_footercontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='footer', to=orm['forms.Form'])),
            ('adress_content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('img', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('copyright', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'project', ['FooterContent'])

        # Adding model 'SocialMedia'
        db.create_table(u'project_socialmedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('footercontent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='socials', to=orm['forms.Form'])),
            ('columns', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=2000, null=True, blank=True)),
            ('footer_social', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('header_social', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'project', ['SocialMedia'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'project_banner')

        # Deleting model 'BannerImg'
        db.delete_table(u'project_bannerimg')

        # Deleting model 'WhatWeDo'
        db.delete_table(u'project_whatwedo')

        # Deleting model 'Realisations'
        db.delete_table(u'project_realisations')

        # Deleting model 'About'
        db.delete_table(u'project_about')

        # Deleting model 'FooterContent'
        db.delete_table(u'project_footercontent')

        # Deleting model 'SocialMedia'
        db.delete_table(u'project_socialmedia')


    models = {
        u'forms.form': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Form', '_ormbases': [u'pages.Page']},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'response': ('mezzanine.core.fields.RichTextField', [], {}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'project.about': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'About'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'about'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'main_title': ('mezzanine.core.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'project.banner': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Banner'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'about_desc': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'about_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'copyright': ('mezzanine.core.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'footer'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'project.realisations': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Realisations'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realisations'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'what_do'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['project']