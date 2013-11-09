# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'pymafia_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Setup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'pymafia', ['Game'])

        # Adding model 'Setup'
        db.create_table(u'pymafia_setup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('num_players', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('is_start_time_day', self.gf('django.db.models.fields.BooleanField')()),
            ('setup_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'pymafia', ['Setup'])

        # Adding model 'SetupKlass'
        db.create_table(u'pymafia_setupklass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('setup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Setup'])),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Klass'])),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'pymafia', ['SetupKlass'])

        # Adding model 'Klass'
        db.create_table(u'pymafia_klass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'pymafia', ['Klass'])

        # Adding model 'Alignment'
        db.create_table(u'pymafia_alignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pymafia', ['Alignment'])

        # Adding model 'Skill'
        db.create_table(u'pymafia_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'pymafia', ['Skill'])

        # Adding model 'Player'
        db.create_table(u'pymafia_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Game'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Klass'])),
        ))
        db.send_create_signal(u'pymafia', ['Player'])

        # Adding model 'Action'
        db.create_table(u'pymafia_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('executor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actions_as_executor', to=orm['pymafia.Player'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actions_as_target', to=orm['pymafia.Player'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pymafia.Skill'])),
        ))
        db.send_create_signal(u'pymafia', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'pymafia_game')

        # Deleting model 'Setup'
        db.delete_table(u'pymafia_setup')

        # Deleting model 'SetupKlass'
        db.delete_table(u'pymafia_setupklass')

        # Deleting model 'Klass'
        db.delete_table(u'pymafia_klass')

        # Deleting model 'Alignment'
        db.delete_table(u'pymafia_alignment')

        # Deleting model 'Skill'
        db.delete_table(u'pymafia_skill')

        # Deleting model 'Player'
        db.delete_table(u'pymafia_player')

        # Deleting model 'Action'
        db.delete_table(u'pymafia_action')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pymafia.action': {
            'Meta': {'object_name': 'Action'},
            'executor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions_as_executor'", 'to': u"orm['pymafia.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Skill']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions_as_target'", 'to': u"orm['pymafia.Player']"})
        },
        u'pymafia.alignment': {
            'Meta': {'object_name': 'Alignment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pymafia.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'setup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Setup']"})
        },
        u'pymafia.klass': {
            'Meta': {'object_name': 'Klass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'pymafia.player': {
            'Meta': {'object_name': 'Player'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Klass']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'pymafia.setup': {
            'Meta': {'object_name': 'Setup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_start_time_day': ('django.db.models.fields.BooleanField', [], {}),
            'klasses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pymafia.Klass']", 'through': u"orm['pymafia.SetupKlass']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'num_players': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'setup_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'pymafia.setupklass': {
            'Meta': {'object_name': 'SetupKlass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Klass']"}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'setup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pymafia.Setup']"})
        },
        u'pymafia.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['pymafia']