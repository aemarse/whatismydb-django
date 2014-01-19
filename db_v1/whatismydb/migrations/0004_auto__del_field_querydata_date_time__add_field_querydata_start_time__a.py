# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'QueryData.date_time'
        db.delete_column(u'whatismydb_querydata', 'date_time')

        # Adding field 'QueryData.start_time'
        db.add_column(u'whatismydb_querydata', 'start_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 19, 0, 0)),
                      keep_default=False)

        # Adding field 'QueryData.end_time'
        db.add_column(u'whatismydb_querydata', 'end_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 19, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'QueryData.date_time'
        db.add_column(u'whatismydb_querydata', 'date_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 19, 0, 0)),
                      keep_default=False)

        # Deleting field 'QueryData.start_time'
        db.delete_column(u'whatismydb_querydata', 'start_time')

        # Deleting field 'QueryData.end_time'
        db.delete_column(u'whatismydb_querydata', 'end_time')


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
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'time_intervals': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whatismydb.TimeIntervals']"})
        },
        u'whatismydb.timeintervals': {
            'Meta': {'object_name': 'TimeIntervals'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['whatismydb']