from django.db import models
from django.forms import ModelForm

#temp observation db
#_______________________________________

class TempFormSlip(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, default='4')
    SLIP_TYPE = (
        ('0','Normal'),
    )
    slipType = models.CharField(max_length=1, choices=SLIP_TYPE, default='0')
    hv_ratio = models.CharField(max_length=100, default='1:3.75')
    rake = models.CharField(max_length=100)
    net_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    dip_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    marker_age = models.CharField(max_length=100)
    SLIP_RATE_CAT = (
        ('0','0.001 <0.01'),
        ('1','0.01 <0.1'),
        ('2','0.1 <1'),
        ('3','1 <5'),
        ('4','5 <10'),
        ('5','10 <50'),
        ('6','50 <100'),
        ('7','100 <200'),
    )
    slip_rate_category = models.CharField(max_length=10, choices=SLIP_RATE_CAT, default='0')
    strike_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    vertical_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    site = models.CharField(max_length=100, default='-42.375, 176.543')
    notes = models.TextField()
 
class TempFormDisp(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, default='0')
    aseismicSlipFactor = models.CharField(max_length=100, default='pref, min, max')
    dip_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    hv_ratio = models.CharField(max_length=100, default='1:3.75')
    marker_age = models.CharField(max_length=100)
    rake = models.CharField(max_length=100)
    SLIP_RATE_CAT = (
        ('0','0.001 <0.01'),
        ('1','0.01 <0.1'),
        ('2','0.1 <1'),
        ('3','1 <5'),
        ('4','5 <10'),
        ('5','10 <50'),
        ('6','50 <100'),
        ('7','100 <200'),
    )
    slip_rate_category = models.CharField(max_length=10, choices=SLIP_RATE_CAT, default='0')
    strike_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    vertical_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    site = models.CharField(max_length=100, default='-42.375, 176.543')
    notes = models.TextField()

# faulted_earth db
#_______________________________________

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256)
    f_table_schema = models.CharField(max_length=256)
    f_table_name = models.CharField(max_length=256)
    f_geometry_column = models.CharField(max_length=256)
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.CharField(max_length=30)
    class Meta:
        db_table = u'geometry_columns'

class SpatialRefSys(models.Model):
    auth_name = models.CharField(max_length=256)
    auth_srid = models.IntegerField()
    srtext = models.CharField(max_length=2048)
    proj4text = models.CharField(max_length=2048)
    class Meta:
        db_table = u'spatial_ref_sys'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField() # This field type is a guess.
    f_table_schema = models.TextField() # This field type is a guess.
    f_table_name = models.TextField() # This field type is a guess.
    f_geography_column = models.TextField() # This field type is a guess.
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.TextField()
    class Meta:
        db_table = u'geography_columns'
        
class Databasechangelog(models.Model):
    id_1 = models.CharField(max_length=63)
    author = models.CharField(max_length=63)
    filename = models.CharField(max_length=200)
    dateexecuted = models.DateTimeField()
    orderexecuted = models.IntegerField()
    exectype = models.CharField(max_length=10)
    md5sum = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    liquibase = models.CharField(max_length=20)
    class Meta:
        db_table = u'databasechangelog'
    

class Databasechangeloglock(models.Model):
    locked = models.BooleanField()
    lockgranted = models.DateTimeField()
    lockedby = models.CharField(max_length=255)
    class Meta:
        db_table = u'databasechangeloglock'

class DataCompletion(models.Model):
    completion = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'data_completion'

class AgeCategory(models.Model):
    age = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'age_category'


class Octant(models.Model):
    octant = models.CharField(max_length=2)
    class Meta:
        db_table = u'octant'
        
class SlipType(models.Model):
    slip_type = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'slip_type'
        
class SectionTrace(models.Model):
    # neotectonic_section = models.ForeignKey(NeotectonicSection)
    accuracy = models.TextField() # This field type is a guess.
    # expression = models.ForeignKey(GeomorphicExpression)
    # location_method = models.ForeignKey(LocationMethod)
    name = models.CharField(max_length=96)
    notes = models.CharField(max_length=254)
    compilation_scale = models.IntegerField()
    geom = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'section_trace'

class SeismogenicGeometry(models.Model):
    # neotectonic_section = models.ForeignKey(NeotectonicSection)
    dip = models.IntegerField()
    # downside = models.ForeignKey(Octant)
    length = models.DecimalField(max_digits=30, decimal_places=3)
    lower_depth = models.DecimalField(max_digits=5, decimal_places=3)
    strike = models.IntegerField()
    upper_depth = models.DecimalField(max_digits=5, decimal_places=3)
    class Meta:
        db_table = u'seismogenic_geometry'
        
class Slip(models.Model):
    dip_slip_rate = models.DecimalField(max_digits=3, decimal_places=2)
    hv_ratio = models.DecimalField(max_digits=3, decimal_places=2)
    marker_age = models.IntegerField()
    rake = models.IntegerField()
    strike_slip_rate = models.DecimalField(max_digits=3, decimal_places=2)
    vertical_slip_rate = models.DecimalField(max_digits=3, decimal_places=2)

class FaultSource(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=3)
    aseismic_slip_factor = models.DecimalField(max_digits=3, decimal_places=2)
    #compiler = models.ForeignKey(PublicUser)
    #completion = models.ForeignKey(DataCompletion)
    #contributor = models.ForeignKey(PublicUser)
    dip = models.TextField() # This field type is a guess.
    dip_dir = models.SmallIntegerField()
    last_movement = models.TextField() # This field type is a guess.
    length = models.DecimalField(max_digits=6, decimal_places=2)
    lower_sm_depth = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=96)
    rake = models.TextField() # This field type is a guess.
    slip_rate = models.TextField() # This field type is a guess.
    slip_type_id = models.SmallIntegerField()
    upper_sm_depth = models.TextField() # This field type is a guess.
    width = models.DecimalField(max_digits=10, decimal_places=3)
    created_date = models.DateField()
    modified_date = models.DateField()
    fault_zone = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'fault_source'
                             
class FaultSummary(models.Model):
    aseismic_slip_factor = models.DecimalField(max_digits=3, decimal_places=2)
    completion = models.ForeignKey(DataCompletion)
    dip = models.IntegerField() # This field type is a guess.
    dip_dir = models.SmallIntegerField()
    displacement = models.IntegerField() # should be DecimalField 
    downthrown_side = models.ForeignKey(Octant)
    is_active = models.BooleanField()
    is_episodic = models.BooleanField()
    is_section_summary = models.BooleanField()
    last_movement = models.IntegerField() # This field type is a guess.
    length = models.DecimalField(max_digits=6, decimal_places=2)
    lower_sm_depth = models.IntegerField() # should be DecimalField 
    name = models.CharField(max_length=96)
    recurrence_interval = models.IntegerField() # This field type is a guess.
    slip_rate = models.IntegerField() # should be DecimalField 
    slip_type = models.ForeignKey(SlipType)
    strike = models.SmallIntegerField()
    upper_sm_depth = models.IntegerField() # should be DecimalField 
    created_date = models.DateField()
    modified_date = models.DateField()
    class Meta:
        db_table = 'GEM\".\"fault_summary'
    
class BlindFaultSummary(models.Model):
    aseismic_slip_factor = models.DecimalField(max_digits=3, decimal_places=2)
    #compiler = models.ForeignKey(PublicUser)
    #completion = models.ForeignKey(DataCompletion)
    #contributor = models.ForeignKey(PublicUser)
    dip = models.TextField() # This field type is a guess.
    dip_dir = models.SmallIntegerField()
    displacement = models.TextField() # This field type is a guess.
    is_active = models.BooleanField()
    is_episodic = models.BooleanField()
    last_movement = models.TextField() # This field type is a guess.
    length = models.DecimalField(max_digits=6, decimal_places=2)
    lower_sm_depth = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=96)
    recurrence_interval = models.TextField() # This field type is a guess.
    slip_rate = models.TextField() # This field type is a guess.
    slip_type = models.ForeignKey(SlipType)
    strike = models.SmallIntegerField()
    upper_sm_depth = models.TextField() # This field type is a guess.
    created_date = models.DateField()
    modified_date = models.DateField()
    polygon = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'blind_fault_summary'

class FaultSynopsis(models.Model):
    fault_summary = models.ForeignKey(FaultSummary)
    location = models.CharField(max_length=254)
    name_origin = models.CharField(max_length=254)
    synopsis = models.CharField(max_length=254)
    class Meta:
        db_table = u'fault_synopsis'

class GeomorphicExpression(models.Model):
    expression = models.CharField(unique=True, max_length=64)
    class Meta:
        db_table = u'geomorphic_expression'

class LocationMethod(models.Model):
    method = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'location_method'
        
class NeotectonicSection(models.Model):
    fault_summary = models.ForeignKey(FaultSummary)
    average_dip = models.IntegerField() # This field type is a guess.
    is_active = models.BooleanField()
    is_episodic = models.BooleanField()
    surface_dip = models.IntegerField() # This field type is a guess.
    name = models.CharField(max_length=96)
    class Meta:
        db_table = u'neotectonic_section'
    
class Event(models.Model):
    neotectonic_section = models.ForeignKey(NeotectonicSection)
    category = models.ForeignKey(AgeCategory)
    historical_eq = models.IntegerField() # This field type is a guess.
    prehistorical_eq = models.IntegerField() # This field type is a guess.
    class Meta:
        db_table = u'event'
        
class FoldType(models.Model):
    fold_type = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'fold_type'

class Fold(models.Model):
    completion = models.ForeignKey(DataCompletion)
    dip_axial_plane = models.IntegerField()
    dip_dir_shallow_limb = models.SmallIntegerField()
    dip_dir_steep_limb = models.SmallIntegerField()
    dip_shallow_limb = models.SmallIntegerField() # This field type is a guess.
    dip_steep_limb = models.SmallIntegerField() # This field type is a guess.
    growth_horizontal = models.IntegerField() # should be DecimalField 
    growth_vertical = models.TextField() # This field type is a guess.
    is_active = models.BooleanField()
    is_episodic = models.BooleanField()
    last_movement = models.TextField() # This field type is a guess.
    last_movement_cat = models.ForeignKey(AgeCategory)
    length = models.IntegerField() #should be DecimalField 
    name = models.CharField(max_length=96)
    plunge = models.TextField() # This field type is a guess.
    plunge_dir = models.IntegerField()
    surface_age = models.IntegerField()
    tilt_shallow_limb = models.DecimalField(max_digits=100, decimal_places=100)
    tilt_steep_limb = models.DecimalField(max_digits=100, decimal_places=100)
    type = models.ForeignKey(FoldType)
    created_date = models.DateField()
    modified_date = models.DateField()
    class Meta:
        db_table = u'fold'   

class ObservationType(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    name = models.CharField(max_length=1, 
                                choices=OBS_TYPE, default='0')
    #name = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'observation_type'
        
class Parameter(models.Model):
    observation_type = models.ForeignKey(ObservationType)
    description = models.CharField(max_length=128)
    name = models.CharField(max_length=24)
    class Meta:
        db_table = u'parameter'

class ParameterDerivation(models.Model):
    parameter = models.ForeignKey(Parameter)
    derivation_type_id = models.SmallIntegerField()
    derivation = models.CharField(max_length=254)
    class Meta:
        db_table = u'parameter_derivation'
        
class RecurrenceIntervalCategory(models.Model):
    interval = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'recurrence_interval_category'

class RecurrenceIntervalType(models.Model):
    type = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'recurrence_interval_type'

class RecurrenceInterval(models.Model):
    neotectonic_section = models.ForeignKey(NeotectonicSection)
    category = models.ForeignKey(RecurrenceIntervalCategory)
    selected = models.BooleanField()
    type = models.ForeignKey(RecurrenceIntervalType)
    value = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'recurrence_interval'
        
class Observation(models.Model):
    entity_id = models.SmallIntegerField()
    observation_type = models.ForeignKey(ObservationType)
    section_id = models.SmallIntegerField()
    site_id = models.SmallIntegerField()
    class Meta:
        db_table = u'observation'

class SlipRateCategory(models.Model):
    slip_rate = models.CharField(unique=True, max_length=24)
    class Meta:
        db_table = u'slip_rate_category'

class CompilationNote(models.Model):
    observation = models.ForeignKey(Observation)
    note = models.CharField(max_length=254)
    class Meta:
        db_table = u'compilation_note'

class DisplacementCategory(models.Model):
    displacement = models.CharField(unique=True, max_length=12)
    class Meta:
        db_table = u'displacement_category'

class Site(models.Model):
    name = models.CharField(max_length=96)
    scale = models.IntegerField()
    accuracy = models.TextField() # This field type is a guess.
    notes = models.CharField(max_length=254)
    geom = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'site'

