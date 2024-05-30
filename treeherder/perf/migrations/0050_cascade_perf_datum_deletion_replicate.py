# Generated by Django 3.0.8 on 2020-12-11 14:42

from django.db import migrations

DATUM_REPLICATE_CONSTRAINT_SYMBOL = (
    'performance_datum_re_performance_datum_id_fe2ed518_fk_performan'
)


class Migration(migrations.Migration):
    dependencies = [
        ('perf', '0049_performancedatumreplicate'),
    ]

    operations = [
        migrations.RunSQL(
            # add ON DELETE CASCADE at database level
            [
                f'ALTER TABLE performance_datum_replicate '
                f'DROP CONSTRAINT {DATUM_REPLICATE_CONSTRAINT_SYMBOL};',
                f'ALTER TABLE performance_datum_replicate '
                f'ADD CONSTRAINT {DATUM_REPLICATE_CONSTRAINT_SYMBOL} '
                f'FOREIGN KEY (performance_datum_id) REFERENCES performance_datum (ID) ON DELETE CASCADE;',
            ],
            # put back the non-CASCADE foreign key constraint
            reverse_sql=[
                f'ALTER TABLE performance_datum_replicate '
                f'DROP CONSTRAINT {DATUM_REPLICATE_CONSTRAINT_SYMBOL};',
                f'ALTER TABLE performance_datum_replicate '
                f'ADD CONSTRAINT {DATUM_REPLICATE_CONSTRAINT_SYMBOL} '
                f'FOREIGN KEY (performance_datum_id) REFERENCES performance_datum (ID);',
            ],
        )
    ]
