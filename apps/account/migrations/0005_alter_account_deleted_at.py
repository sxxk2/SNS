# Generated by Django 4.0.6 on 2022-08-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]