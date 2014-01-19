# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DayData'
        db.create_table(u'whatismydb_daydata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'whatismydb', ['DayData'])

        # Adding model 'MinuteData'
        db.create_table(u'whatismydb_minutedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'whatismydb', ['MinuteData'])

        # Adding model 'HourData'
        db.create_table(u'whatismydb_hourdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'whatismydb', ['HourData'])


    def backwards(self, orm):
        # Deleting model 'DayData'
        db.delete_table(u'whatismydb_daydata')

        # Deleting model 'MinuteData'
        db.delete_table(u'whatismydb_minutedata')

        # Deleting model 'HourData'
        db.delete_table(u'whatismydb_hourdata')


    models = {
        u'whatismydb.daydata': {
            'Meta': {'object_name': 'DayData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'whatismydb.hourdata': {
            'Meta': {'object_name': 'HourData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'whatismydb.minutedata': {
            'Meta': {'object_name': 'MinuteData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['whatismydb']