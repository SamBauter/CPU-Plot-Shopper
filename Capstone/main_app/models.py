# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import csv
from django.db import models


def populate_MonSpec_from_csv(path='main_app/static/df_csvs/cleaned_monitors.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = MonitorSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    size=None if row[2] == "" else float(row[2]),
                    resolution=None if row[3] == "" else row[3],
                    ref_rate=None if row[4] == "" else int(float(row[4])),
                    res_rate=None if row[5] == "" else float(row[5]),
                    panel_type=None if row[6] == "" else row[6],
                    asp_ratio=None if row[7] == "" else row[7],
                    price=None if row[8] == "" else float(row[8]),
                    curved=None if row[9] == "" else row[9],
                    g_sync_compat=None if row[10] == "" else row[10],
                    sync=None if row[11] == "" else row[11]

                )


def populate_CPUSpec_from_csv(path='main_app/static/df_csvs/cpus.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = CPUSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    core_count=None if row[2] == "" else int(row[2]),
                    core_clock=None if row[3] == "" else float(row[3]),
                    boost_clock=None if row[4] == "" else float(row[4]),
                    tdp=None if row[5] == "" else int(row[5]),
                    integrated_graphics=None if row[6] == "None" else row[6],
                    smt=None if row[7] == "" else row[7],
                    price=None if row[8] == "" else float(row[8]),
                )


def populate_MBSpec_from_csv(path='main_app/static/df_csvs/motherboards.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = MBSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    socket=None if row[2] == "" else row[2],
                    form_factor=None if row[3] == "" else row[3],
                    mem_max=None if row[4] == "" else int(row[4]),
                    mem_slots=None if row[5] == "" else int(row[5]),
                    color=None if row[6] == "None" else row[6],
                    price=None if row[7] == "" else float(row[7]),
                )


def populate_PSUSpec_from_csv(path='main_app/static/df_csvs/psus.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = PSUSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    form_factor=None if row[2] == "" else row[2],
                    eff_rating=None if row[3] == "" else row[3],
                    wattage=None if row[4] == "" else int(row[4]),
                    modular=None if row[5] == "" else row[5],
                    color=None if row[6] == "None" else row[6],
                    price=None if row[7] == "" else float(row[7]),
                )


def populate_RAMSpec_from_csv(path='main_app/static/df_csvs/rams.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = RAMSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    speed=None if row[2] == "" else row[2],
                    modules=None if row[3] == "" else row[3],
                    price_per_gb=None if row[4] == "" else float(row[4]),
                    color=None if row[5] == "" else row[5],
                    first_word_lat=None if row[6] == "" else float(row[6]),
                    cas_lat=None if row[7] == "" else int(float(row[7])),
                    price=None if row[8] == "" else float(row[8]),
                )


def populate_StorSpec_from_csv(path='main_app/static/df_csvs/storages.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = StorSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    capacity=None if row[2] == "" else row[2],
                    price_per_gb=None if row[3] == "" else float(row[3]),
                    drive_type=None if row[4] == "" else row[4],
                    cache=None if row[5] == "" else int(row[5]),
                    form_factor=None if row[6] == "" else row[6],
                    interface=None if row[7] == "" else row[7],
                    price=None if row[8] == "" else float(row[8]),
                )


def populate_GPUSpec_from_csv(path='main_app/static/df_csvs/gpus.csv'):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'brand':
                _, created = GPUSpecs.objects.get_or_create(
                    brand=row[0],
                    model=row[1],
                    chipset=None if row[2] == "" else row[2],
                    memory=None if row[3] == "" else float(row[3]),
                    core_clock=None if row[4] == "" else int(float(row[4])),
                    boost_clock=None if row[5] == "" else int(float(row[5])),
                    color=None if row[6] == "" else row[6],
                    length=None if row[7] == "" else float(row[7]),
                    price=None if row[8] == "" else float(row[8]),
                )


class CPUSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    core_count = models.IntegerField(blank=True, null=True)
    core_clock = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    boost_clock = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    tdp = models.IntegerField(blank=True, null=True)
    integrated_graphics = models.TextField(blank=True, null=True)
    smt = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


# class MonitorSpecsManager(models.Manager):
#   def getUniqueValues(self, field):
#      return self.values(field).order_by(field).distinct().values_list(field, flat=True)

# def getHeaderVals(self):
#    return self.field


class MonitorSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    size = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)  # This field type is a guess.
    resolution = models.TextField(blank=True, null=True)
    ref_rate = models.IntegerField(blank=True, null=True)
    res_rate = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)  # This field type is a guess.
    panel_type = models.TextField(blank=True, null=True)
    asp_ratio = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # This field type is a guess.
    curved = models.BooleanField(blank=True, null=True)
    g_sync_compat = models.BooleanField(blank=True, null=True)
    sync = models.TextField(blank=True, null=True)

    # objects = MonitorSpecsManager()

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.size) + " " + self.resolution + " " + str(
            self.ref_rate) + "Hz"


class GPUSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    chipset = models.TextField(blank=True, null=True)
    memory = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    core_clock = models.IntegerField(blank=True, null=True)
    boost_clock = models.IntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.chipset)


class MBSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    socket = models.TextField(blank=True, null=True)
    form_factor = models.TextField(blank=True, null=True)
    mem_max = models.IntegerField(blank=True, null=True)
    mem_slots = models.IntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.socket + " " + self.form_factor


class PSUSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    form_factor = models.TextField(blank=True, null=True)
    eff_rating = models.TextField(blank=True, null=True)
    wattage = models.IntegerField(blank=True, null=True)
    modular = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.form_factor + " " + self.eff_rating


class RAMSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    speed = models.TextField(blank=True, null=True)
    modules = models.TextField(blank=True, null=True)
    price_per_gb = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    color = models.TextField(blank=True, null=True)
    first_word_lat = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    cas_lat = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.speed + " " + self.modules


class StorSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    capacity = models.TextField(blank=True, null=True)
    price_per_gb = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    drive_type = models.TextField(blank=True, null=True)
    cache = models.IntegerField(blank=True, null=True)
    form_factor = models.TextField(blank=True, null=True)
    interface = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.capacity + " " + self.drive_type + " " + self.interface


db_counts = {'monitor_count': MonitorSpecs.objects.all().count(),
             'cpu_count': CPUSpecs.objects.all().count(),
             'gpu_count': GPUSpecs.objects.all().count(),
             'mb_count': MBSpecs.objects.all().count(),
             'psu_count': PSUSpecs.objects.all().count(),
             'ram_count': RAMSpecs.objects.all().count(),
             'stor_count': StorSpecs.objects.all().count()}
