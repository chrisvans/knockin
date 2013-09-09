# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Passcode.lockout_time'
        db.add_column(u'padkey_passcode', 'lockout_time',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Passcode.lockout_time'
        db.delete_column(u'padkey_passcode', 'lockout_time')


    models = {
        u'padkey.passcode': {
            'Meta': {'object_name': 'Passcode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lockout_time': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'passcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['padkey']