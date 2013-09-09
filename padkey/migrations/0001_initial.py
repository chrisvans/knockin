# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Passcode'
        db.create_table(u'padkey_passcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passcode', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'padkey', ['Passcode'])


    def backwards(self, orm):
        # Deleting model 'Passcode'
        db.delete_table(u'padkey_passcode')


    models = {
        u'padkey.passcode': {
            'Meta': {'object_name': 'Passcode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['padkey']