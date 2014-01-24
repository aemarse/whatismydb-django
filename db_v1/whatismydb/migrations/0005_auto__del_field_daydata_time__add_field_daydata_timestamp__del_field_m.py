# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DayData.time'
        db.delete_column(u'whatismydb_daydata', 'time')

        # Adding field 'DayData.timestamp'
        db.add_column(u'whatismydb_daydata', 'timestamp',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Deleting field 'MinuteData.time'
        db.delete_column(u'whatismydb_minutedata', 'time')

        # Adding field 'MinuteData.timestamp'
        db.add_column(u'whatismydb_minutedata', 'timestamp',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Deleting field 'HourData.time'
        db.delete_column(u'whatismydb_hourdata', 'time')

        # Adding field 'HourData.timestamp'
        db.add_column(u'whatismydb_hourdata', 'timestamp',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DayData.time'
        db.add_column(u'whatismydb_daydata', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 23, 0, 0)),
                      keep_default=False)

        # Deleting field 'DayData.timestamp'
        db.delete_column(u'whatismydb_daydata', 'timestamp')

        # Adding field 'MinuteData.time'
        db.add_column(u'whatismydb_minutedata', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 23, 0, 0)),
                      keep_default=False)

        # Deleting field 'MinuteData.timestamp'
        db.delete_column(u'whatismydb_minutedata', 'timestamp')

        # Adding field 'HourData.time'
        db.add_column(u'whatismydb_hourdata', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 23, 0, 0)),
                      keep_default=False)

        # Deleting field 'HourData.timestamp'
        db.delete_column(u'whatismydb_hourdata', 'timestamp')


    models = {
        u'whatismydb.daydata': {
            'Meta': {'object_name': 'DayData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'whatismydb.hourdata': {
            'Meta': {'object_name': 'HourData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'whatismydb.minutedata': {
            'Meta': {'object_name': 'MinuteData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.FloatField', [], {}),
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