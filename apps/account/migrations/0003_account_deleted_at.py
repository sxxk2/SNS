# Generated by Django 4.0.6 on 2022-07-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_name_account_account_name_account_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
