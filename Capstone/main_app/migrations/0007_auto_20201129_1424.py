# Generated by Django 3.1.3 on 2020-11-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201129_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramspecs',
            name='first_word_lat',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]
