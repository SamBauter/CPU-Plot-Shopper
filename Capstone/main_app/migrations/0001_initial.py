# Generated by Django 3.1.3 on 2020-11-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('core_count', models.IntegerField(blank=True, null=True)),
                ('boost_clock', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('tdp', models.IntegerField(blank=True, null=True)),
                ('integrated_graphics', models.TextField(blank=True, null=True)),
                ('smt', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GPUSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('chipset', models.TextField(blank=True, null=True)),
                ('memory', models.IntegerField(blank=True, null=True)),
                ('core_clock', models.IntegerField(blank=True, null=True)),
                ('boost_clock', models.IntegerField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MBSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('socket', models.TextField(blank=True, null=True)),
                ('form_factor', models.TextField(blank=True, null=True)),
                ('mem_max', models.IntegerField(blank=True, null=True)),
                ('mem_slots', models.IntegerField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('size', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('ref_rate', models.IntegerField(blank=True, null=True)),
                ('res_rate', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('panel_type', models.TextField(blank=True, null=True)),
                ('asp_ratio', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('curved', models.BooleanField(blank=True, null=True)),
                ('g_sync_compat', models.BooleanField(blank=True, null=True)),
                ('sync', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PSUSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('form_factor', models.TextField(blank=True, null=True)),
                ('eff_rating', models.TextField(blank=True, null=True)),
                ('wattage', models.IntegerField(blank=True, null=True)),
                ('modular', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RAMSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('speed', models.TextField(blank=True, null=True)),
                ('modules', models.TextField(blank=True, null=True)),
                ('price_per_gb', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('first_word_lat', models.IntegerField(blank=True, null=True)),
                ('cas_lat', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StorSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('capacity', models.TextField(blank=True, null=True)),
                ('price_per_gb', models.TextField(blank=True, null=True)),
                ('drive_type', models.TextField(blank=True, null=True)),
                ('cache', models.IntegerField(blank=True, null=True)),
                ('form_factor', models.TextField(blank=True, null=True)),
                ('interface', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
