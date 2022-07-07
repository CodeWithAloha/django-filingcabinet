# Generated by Django 3.2.14 on 2022-07-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filingcabinet", "0022_auto_20210603_1617"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="collectiondocument",
            constraint=models.UniqueConstraint(
                fields=("collection", "document"),
                name="unique_doc_collection_filingcabinet_collectiondocument",
            ),
        ),
    ]
