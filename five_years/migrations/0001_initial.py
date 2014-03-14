# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table(u'five_years_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'five_years', ['Source'])

        # Adding model 'Income'
        db.create_table(u'five_years_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Source'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['Income'])

        # Adding model 'LivingExpense'
        db.create_table(u'five_years_livingexpense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Income'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.SmallIntegerField')(default=1, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('done_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['LivingExpense'])

        # Adding model 'InterpersonalCircle'
        db.create_table(u'five_years_interpersonalcircle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Income'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.SmallIntegerField')(default=1, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('done_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['InterpersonalCircle'])

        # Adding model 'ExtendKnowledge'
        db.create_table(u'five_years_extendknowledge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Income'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.SmallIntegerField')(default=1, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('done_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['ExtendKnowledge'])

        # Adding model 'Holiday'
        db.create_table(u'five_years_holiday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Income'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.SmallIntegerField')(default=1, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('done_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['Holiday'])

        # Adding model 'Saving'
        db.create_table(u'five_years_saving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['five_years.Income'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=25, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.SmallIntegerField')(default=1, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('done_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'five_years', ['Saving'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table(u'five_years_source')

        # Deleting model 'Income'
        db.delete_table(u'five_years_income')

        # Deleting model 'LivingExpense'
        db.delete_table(u'five_years_livingexpense')

        # Deleting model 'InterpersonalCircle'
        db.delete_table(u'five_years_interpersonalcircle')

        # Deleting model 'ExtendKnowledge'
        db.delete_table(u'five_years_extendknowledge')

        # Deleting model 'Holiday'
        db.delete_table(u'five_years_holiday')

        # Deleting model 'Saving'
        db.delete_table(u'five_years_saving')


    models = {
        u'five_years.extendknowledge': {
            'Meta': {'object_name': 'ExtendKnowledge'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['five_years.Source']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '25', 'decimal_places': '2'})
        },
        u'five_years.interpersonalcircle': {
            'Meta': {'object_name': 'InterpersonalCircle'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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