# Generated by Django 2.1.4 on 2019-01-09 12:39

from django.db import migrations

import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("filingcabinet", "0005_auto_20181217_1456"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                related_name="+",
                through="filingcabinet.TaggedDocument",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]