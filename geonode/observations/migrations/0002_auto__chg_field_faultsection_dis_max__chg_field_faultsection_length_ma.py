# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'FaultSection.dis_max'
        db.alter_column('observations_faultsection', 'dis_max', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.length_max'
        db.alter_column('observations_faultsection', 'length_max', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.contrib'
        db.alter_column('observations_faultsection', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.re_int_min'
        db.alter_column('observations_faultsection', 're_int_min', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.u_sm_d_pre'
        db.alter_column('observations_faultsection', 'u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.mov_pref'
        db.alter_column('observations_faultsection', 'mov_pref', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.sec_name'
        db.alter_column('observations_faultsection', 'sec_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FaultSection.length_min'
        db.alter_column('observations_faultsection', 'length_min', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.u_sm_d_com'
        db.alter_column('observations_faultsection', 'u_sm_d_com', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.dip_pref'
        db.alter_column('observations_faultsection', 'dip_pref', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.dip_dir'
        db.alter_column('observations_faultsection', 'dip_dir', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.slip_r_max'
        db.alter_column('observations_faultsection', 'slip_r_max', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.dis_pref'
        db.alter_column('observations_faultsection', 'dis_pref', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.aseis_com'
        db.alter_column('observations_faultsection', 'aseis_com', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.dip_max'
        db.alter_column('observations_faultsection', 'dip_max', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.slip_r_com'
        db.alter_column('observations_faultsection', 'slip_r_com', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.low_d_max'
        db.alter_column('observations_faultsection', 'low_d_max', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.low_d_pref'
        db.alter_column('observations_faultsection', 'low_d_pref', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.dip_com'
        db.alter_column('observations_faultsection', 'dip_com', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.down_thro'
        db.alter_column('observations_faultsection', 'down_thro', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.aseis_slip'
        db.alter_column('observations_faultsection', 'aseis_slip', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.slip_com'
        db.alter_column('observations_faultsection', 'slip_com', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.strike'
        db.alter_column('observations_faultsection', 'strike', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.re_int_max'
        db.alter_column('observations_faultsection', 're_int_max', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.u_sm_d_max'
        db.alter_column('observations_faultsection', 'u_sm_d_max', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.length_pre'
        db.alter_column('observations_faultsection', 'length_pre', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.mov_max'
        db.alter_column('observations_faultsection', 'mov_max', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.re_int_pre'
        db.alter_column('observations_faultsection', 're_int_pre', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.compiler'
        db.alter_column('observations_faultsection', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.episodi_is'
        db.alter_column('observations_faultsection', 'episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.created'
        db.alter_column('observations_faultsection', 'created', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=3))

        # Changing field 'FaultSection.episodi_ac'
        db.alter_column('observations_faultsection', 'episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.dis_min'
        db.alter_column('observations_faultsection', 'dis_min', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.low_d_com'
        db.alter_column('observations_faultsection', 'low_d_com', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.dip_min'
        db.alter_column('observations_faultsection', 'dip_min', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.all_com'
        db.alter_column('observations_faultsection', 'all_com', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.u_sm_d_min'
        db.alter_column('observations_faultsection', 'u_sm_d_min', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.mov_min'
        db.alter_column('observations_faultsection', 'mov_min', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.slip_r_min'
        db.alter_column('observations_faultsection', 'slip_r_min', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FaultSection.low_d_min'
        db.alter_column('observations_faultsection', 'low_d_min', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'FaultSection.slip_r_pre'
        db.alter_column('observations_faultsection', 'slip_r_pre', self.gf('django.db.models.fields.IntegerField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'FaultSection.dis_max'
        db.alter_column('observations_faultsection', 'dis_max', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.length_max'
        db.alter_column('observations_faultsection', 'length_max', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.contrib'
        db.alter_column('observations_faultsection', 'contrib', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

        # Changing field 'FaultSection.re_int_min'
        db.alter_column('observations_faultsection', 're_int_min', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.u_sm_d_pre'
        db.alter_column('observations_faultsection', 'u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.mov_pref'
        db.alter_column('observations_faultsection', 'mov_pref', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.sec_name'
        db.alter_column('observations_faultsection', 'sec_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

        # Changing field 'FaultSection.length_min'
        db.alter_column('observations_faultsection', 'length_min', self.gf('django.db.models.fields.FloatField')(default=''))

        # Changing field 'FaultSection.u_sm_d_com'
        db.alter_column('observations_faultsection', 'u_sm_d_com', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.dip_pref'
        db.alter_column('observations_faultsection', 'dip_pref', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.dip_dir'
        db.alter_column('observations_faultsection', 'dip_dir', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.slip_r_max'
        db.alter_column('observations_faultsection', 'slip_r_max', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.dis_pref'
        db.alter_column('observations_faultsection', 'dis_pref', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.aseis_com'
        db.alter_column('observations_faultsection', 'aseis_com', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.dip_max'
        db.alter_column('observations_faultsection', 'dip_max', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.slip_r_com'
        db.alter_column('observations_faultsection', 'slip_r_com', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.low_d_max'
        db.alter_column('observations_faultsection', 'low_d_max', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.low_d_pref'
        db.alter_column('observations_faultsection', 'low_d_pref', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.dip_com'
        db.alter_column('observations_faultsection', 'dip_com', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.down_thro'
        db.alter_column('observations_faultsection', 'down_thro', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.aseis_slip'
        db.alter_column('observations_faultsection', 'aseis_slip', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.slip_com'
        db.alter_column('observations_faultsection', 'slip_com', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.strike'
        db.alter_column('observations_faultsection', 'strike', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.re_int_max'
        db.alter_column('observations_faultsection', 're_int_max', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.u_sm_d_max'
        db.alter_column('observations_faultsection', 'u_sm_d_max', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.length_pre'
        db.alter_column('observations_faultsection', 'length_pre', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.mov_max'
        db.alter_column('observations_faultsection', 'mov_max', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.re_int_pre'
        db.alter_column('observations_faultsection', 're_int_pre', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.compiler'
        db.alter_column('observations_faultsection', 'compiler', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

        # Changing field 'FaultSection.episodi_is'
        db.alter_column('observations_faultsection', 'episodi_is', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

        # Changing field 'FaultSection.created'
        db.alter_column('observations_faultsection', 'created', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3))

        # Changing field 'FaultSection.episodi_ac'
        db.alter_column('observations_faultsection', 'episodi_ac', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

        # Changing field 'FaultSection.dis_min'
        db.alter_column('observations_faultsection', 'dis_min', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.low_d_com'
        db.alter_column('observations_faultsection', 'low_d_com', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.dip_min'
        db.alter_column('observations_faultsection', 'dip_min', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.all_com'
        db.alter_column('observations_faultsection', 'all_com', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.u_sm_d_min'
        db.alter_column('observations_faultsection', 'u_sm_d_min', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.mov_min'
        db.alter_column('observations_faultsection', 'mov_min', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.slip_r_min'
        db.alter_column('observations_faultsection', 'slip_r_min', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FaultSection.low_d_min'
        db.alter_column('observations_faultsection', 'low_d_min', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'FaultSection.slip_r_pre'
        db.alter_column('observations_faultsection', 'slip_r_pre', self.gf('django.db.models.fields.IntegerField')(default=0))


    models = {
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            'rake_com': ('django.db.models.fields.IntegerField', [], {}),
            'rake_max': ('django.db.models.fields.IntegerField', [], {}),
            'rake_min': ('django.db.models.fields.IntegerField', [], {}),
            'rake_pref': ('django.db.models.fields.IntegerField', [], {}),
            'randomlyfield': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'source_nm': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsourcetrace': {
            'Meta': {'object_name': 'FaultSourceTrace'},
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'observations.faultsummary': {
            'Meta': {'object_name': 'FaultSummary'},
            'fid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': "'-1'", 'max_length': '100', 'blank': 'True'})
        },
        'observations.observations': {
            'Meta': {'object_name': 'Observations'},
            'dip_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hv_ratio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_age': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'observationType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rake': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slipType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slip_rate_category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'strike_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'observations.siteobservation': {
            'Meta': {'object_name': 'SiteObservation'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'observations.trace': {
            'Meta': {'object_name': 'Trace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'tid': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['observations']
