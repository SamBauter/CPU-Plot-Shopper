# Generated by Django 3.1.3 on 2020-11-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201129_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpuspecs',
            name='core_clock',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]