# Generated by Django 4.0.6 on 2022-08-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='계정의 이름'),
        ),
    ]
