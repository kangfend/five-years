# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'InterpersonalCircle.description'
        db.alter_column(u'five_years_interpersonalcircle', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'LivingExpense.description'
        db.alter_column(u'five_years_livingexpense', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Holiday.description'
        db.alter_column(u'five_years_holiday', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Saving.description'
        db.alter_column(u'five_years_saving', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Income.description'
        db.alter_column(u'five_years_income', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ExtendKnowledge.description'
        db.alter_column(u'five_years_extendknowledge', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'InterpersonalCircle.description'
        db.alter_column(u'five_years_interpersonalcircle', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'LivingExpense.description'
        db.alter_column(u'five_years_livingexpense', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Holiday.description'
        db.alter_column(u'five_years_holiday', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Saving.description'
        db.alter_column(u'five_years_saving', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Income.description'
        db.alter_column(u'five_years_income', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ExtendKnowledge.description'
        db.alter_column(u'five_years_extendknowledge', 'description', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        u'five_years.extendknowledge': {
            'Meta': {'object_name': 'ExtendKnowledge'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Income']", 'null': 'True', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.holiday': {
            'Meta': {'object_name': 'Holiday'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Income']", 'null': 'True', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.income': {
            'Meta': {'object_name': 'Income'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Source']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.interpersonalcircle': {
            'Meta': {'object_name': 'InterpersonalCircle'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Income']", 'null': 'True', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.livingexpense': {
            'Meta': {'object_name': 'LivingExpense'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Income']", 'null': 'True', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.saving': {
            'Meta': {'object_name': 'Saving'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Income']", 'null': 'True', 'blank': 'True'}),
            'transaction': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['five_years']