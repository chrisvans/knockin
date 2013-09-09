# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Diagnoser.was_successful'
        db.add_column(u'padkey_diagnoser', 'was_successful',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Diagnoser.was_successful'
        db.delete_column(u'padkey_diagnoser', 'was_successful')


    models = {
        u'padkey.diagnoser': {
            'Meta': {'object_name': 'Diagnoser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'used_passcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'was_successful': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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