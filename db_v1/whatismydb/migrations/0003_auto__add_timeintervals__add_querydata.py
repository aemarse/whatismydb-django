# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeIntervals'
        db.create_table(u'whatismydb_timeintervals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'whatismydb', ['TimeIntervals'])

        # Adding model 'QueryData'
        db.create_table(u'whatismydb_querydata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_intervals', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whatismydb.TimeIntervals'])),
        ))
        db.send_create_signal(u'whatismydb', ['QueryData'])


    def backwards(self, orm):
        # Deleting model 'TimeIntervals'
        db.delete_table(u'whatismydb_timeintervals')

        # Deleting model 'QueryData'
        db.delete_table(u'whatismydb_querydata')


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
        },
        u'whatismydb.querydata': {
            'Meta': {'object_name': 'QueryData'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_intervals': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whatismydb.TimeIntervals']"})
        },
        u'whatismydb.timeintervals': {
            'Meta': {'object_name': 'TimeIntervals'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['whatismydb']