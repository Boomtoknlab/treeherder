# Generated by Django 5.1.5 on 2025-02-27 18:06

import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.functions.text
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("model", "0037_bugjobmap_internal_bug_refs"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="commit",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector(
                    "revision",
                    "author",
                    django.db.models.functions.text.Substr("comments", 1, 100000),
                    config="english",
                ),
                name="search_vector_idx",
            ),
        ),
    ]
