# Generated by Django 3.1.3 on 2020-11-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201129_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpuspecs',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
