# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.delete_table('players_playerdb')

    def backwards(self, orm):
        raise RuntimeError("Cannot revert this migration")

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'players.playerattribute': {
            'Meta': {'object_name': 'PlayerAttribute'},
            'db_date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'db_lock_storage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'db_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['players.PlayerDB']"}),
            'db_value': ('src.utils.picklefield.PickledObjectField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'players.playerdb': {
            'Meta': {'object_name': 'PlayerDB'},
            'db_cmdset_storage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'db_date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_is_connected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'db_lock_storage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'db_permissions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'db_typeclass_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'players.playerdbtmp': {
            'Meta': {'ordering': "['-db_date_created', 'id', 'db_typeclass_path', 'db_key']", 'object_name': 'PlayerDBtmp'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'db_date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'db_is_connected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_cmdset_storage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'db_lock_storage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'db_permissions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'db_typeclass_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'players.playernick': {
            'Meta': {'unique_together': "(('db_nick', 'db_type', 'db_obj'),)", 'object_name': 'PlayerNick'},
            'db_nick': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'db_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['players.PlayerDB']"}),
            'db_real': ('django.db.models.fields.TextField', [], {}),
            'db_type': ('django.db.models.fields.CharField', [], {'default': "'inputline'", 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['players']
