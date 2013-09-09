# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Diagnoser'
        db.create_table(u'padkey_diagnoser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('used_passcode', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'padkey', ['Diagnoser'])


        # Changing field 'Passcode.lockout_time'
        db.alter_column(u'padkey_passcode', 'lockout_time', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):
        # Deleting model 'Diagnoser'
        db.delete_table(u'padkey_diagnoser')


        # Changing field 'Passcode.lockout_time'
        db.alter_column(u'padkey_passcode', 'lockout_time', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'padkey.diagnoser': {
            'Meta': {'object_name': 'Diagnoser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'used_passcode': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'padkey.passcode': {
            'Meta': {'object_name': 'Passcode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lockout_time': ('django.db.models.fields.IntegerField', [], {'default': '900'}),
            'passcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['padkey']