# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FaultSource'
        db.create_table('observations_faultsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_nm', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('length_min', self.gf('django.db.models.fields.FloatField')()),
            ('length_max', self.gf('django.db.models.fields.FloatField')()),
            ('length_pre', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('width', self.gf('django.db.models.fields.FloatField')()),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('rake_min', self.gf('django.db.models.fields.IntegerField')()),
            ('rake_max', self.gf('django.db.models.fields.IntegerField')()),
            ('rake_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('rake_com', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_min', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_max', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_com', self.gf('django.db.models.fields.IntegerField')()),
            ('magnitude', self.gf('django.db.models.fields.IntegerField')()),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')()),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dis_min', self.gf('django.db.models.fields.FloatField')()),
            ('dis_max', self.gf('django.db.models.fields.FloatField')()),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')()),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('all_com', self.gf('django.db.models.fields.IntegerField')()),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('created', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
        ))
        db.send_create_signal('observations', ['FaultSource'])

        # Adding model 'FaultSourceTrace'
        db.create_table('observations_faultsourcetrace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')()),
        ))
        db.send_create_signal('observations', ['FaultSourceTrace'])

        # Adding model 'Fault'
        db.create_table('observations_fault', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fault_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('length_min', self.gf('django.db.models.fields.FloatField')()),
            ('length_max', self.gf('django.db.models.fields.FloatField')()),
            ('length_pre', self.gf('django.db.models.fields.FloatField')()),
            ('strike', self.gf('django.db.models.fields.IntegerField')()),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('down_thro', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_min', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_max', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_com', self.gf('django.db.models.fields.IntegerField')()),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')()),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dis_min', self.gf('django.db.models.fields.FloatField')()),
            ('dis_max', self.gf('django.db.models.fields.FloatField')()),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')()),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('all_com', self.gf('django.db.models.fields.IntegerField')()),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('created', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
        ))
        db.send_create_signal('observations', ['Fault'])

        # Adding model 'FaultSection'
        db.create_table('observations_faultsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sec_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('length_min', self.gf('django.db.models.fields.FloatField')()),
            ('length_max', self.gf('django.db.models.fields.FloatField')()),
            ('length_pre', self.gf('django.db.models.fields.FloatField')()),
            ('strike', self.gf('django.db.models.fields.IntegerField')()),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')()),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')()),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')()),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('down_thro', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_min', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_max', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('slip_r_com', self.gf('django.db.models.fields.IntegerField')()),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')()),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')()),
            ('dis_min', self.gf('django.db.models.fields.FloatField')()),
            ('dis_max', self.gf('django.db.models.fields.FloatField')()),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')()),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')()),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')()),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')()),
            ('all_com', self.gf('django.db.models.fields.IntegerField')()),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('created', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
        ))
        db.send_create_signal('observations', ['FaultSection'])

        # Adding M2M table for field fault on 'FaultSection'
        db.create_table('observations_faultsection_fault', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False)),
            ('fault', models.ForeignKey(orm['observations.fault'], null=False))
        ))
        db.create_unique('observations_faultsection_fault', ['faultsection_id', 'fault_id'])

        # Adding model 'Trace'
        db.create_table('observations_trace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tid', self.gf('django.db.models.fields.IntegerField')()),
            ('loc_meth', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('scale', self.gf('django.db.models.fields.BigIntegerField')()),
            ('accuracy', self.gf('django.db.models.fields.BigIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')()),
        ))
        db.send_create_signal('observations', ['Trace'])

        # Adding M2M table for field fault_section on 'Trace'
        db.create_table('observations_trace_fault_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trace', models.ForeignKey(orm['observations.trace'], null=False)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False))
        ))
        db.create_unique('observations_trace_fault_section', ['trace_id', 'faultsection_id'])

        # Adding model 'SiteObservation'
        db.create_table('observations_siteobservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')()),
            ('scale', self.gf('django.db.models.fields.BigIntegerField')()),
            ('accuracy', self.gf('django.db.models.fields.BigIntegerField')()),
            ('s_feature', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('observations', ['SiteObservation'])

        # Adding M2M table for field fault_section on 'SiteObservation'
        db.create_table('observations_siteobservation_fault_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('siteobservation', models.ForeignKey(orm['observations.siteobservation'], null=False)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False))
        ))
        db.create_unique('observations_siteobservation_fault_section', ['siteobservation_id', 'faultsection_id'])

        # Adding model 'Observations'
        db.create_table('observations_observations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observationType', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('slipType', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('hv_ratio', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('rake', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('net_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('net_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('net_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('marker_age', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slip_rate_category', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('strike_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('strike_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('strike_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('vertical_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('vertical_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('vertical_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('summary_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('observations', ['Observations'])

        # Adding model 'FaultSummary'
        db.create_table('observations_faultsummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.IntegerField')(default='-1', max_length=100, blank=True)),
        ))
        db.send_create_signal('observations', ['FaultSummary'])


    def backwards(self, orm):
        
        # Deleting model 'FaultSource'
        db.delete_table('observations_faultsource')

        # Deleting model 'FaultSourceTrace'
        db.delete_table('observations_faultsourcetrace')

        # Deleting model 'Fault'
        db.delete_table('observations_fault')

        # Deleting model 'FaultSection'
        db.delete_table('observations_faultsection')

        # Removing M2M table for field fault on 'FaultSection'
        db.delete_table('observations_faultsection_fault')

        # Deleting model 'Trace'
        db.delete_table('observations_trace')

        # Removing M2M table for field fault_section on 'Trace'
        db.delete_table('observations_trace_fault_section')

        # Deleting model 'SiteObservation'
        db.delete_table('observations_siteobservation')

        # Removing M2M table for field fault_section on 'SiteObservation'
        db.delete_table('observations_siteobservation_fault_section')

        # Deleting model 'Observations'
        db.delete_table('observations_observations')

        # Deleting model 'FaultSummary'
        db.delete_table('observations_faultsummary')


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
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
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
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
