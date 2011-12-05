# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute("""
        CREATE TABLE gem.gt_pk_metadata (
            table_schema VARCHAR(32) NOT NULL,
            table_name VARCHAR(32) NOT NULL,
            pk_column VARCHAR(32) NOT NULL,
            pk_column_idx INTEGER,
            pk_policy VARCHAR(32),
            pk_sequence VARCHAR(64),
            unique (table_schema, table_name, pk_column),
            check (pk_policy in ('sequence', 'assigned', 'autoincrement'))
        )
        """)
        db.execute("""
        INSERT INTO
            gem.gt_pk_metadata (table_schema, table_name, pk_column)
        VALUES
            ('gem', 'fault_section_view', 'id')
        """)


    def backwards(self, orm):
        db.execute("DROP TABLE gem.gt_pk_metadata")


    models = {}

    complete_apps = ['observations']
