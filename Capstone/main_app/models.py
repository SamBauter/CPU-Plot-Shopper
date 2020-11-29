# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MonitorSpecsManager(models.Manager):
    def getUniqueValues(self, field):
        return self.values(field).order_by(field).distinct().values_list(field, flat=True)

    def getHeaderVals(self):
        return self.field


class MonitorSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    size = models.DecimalField(max_digits=6, decimal_places=1, null=True)  # This field type is a guess.
    resolution = models.TextField(blank=True, null=True)
    ref_rate = models.IntegerField(blank=True, null=True)
    res_rate = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)  # This field type is a guess.
    panel_type = models.TextField(blank=True, null=True)
    asp_ratio = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # This field type is a guess.
    curved = models.BooleanField(blank=True, null=True)
    g_sync = models.BooleanField(blank=True, null=True)
    g_sync_compat = models.BooleanField(blank=True, null=True)
    g_sync_ultimate = models.BooleanField(blank=True, null=True)
    free_sync = models.BooleanField(blank=True, null=True)
    free_sync_premium = models.BooleanField(blank=True, null=True)
    free_sync_premium_pro = models.BooleanField(blank=True, null=True)
    objects = MonitorSpecsManager()

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.size) + " " + self.resolution + " " + str(
            self.ref_rate) + "Hz"

    class Meta:
        managed = True
        db_table = 'MonitorSpecs'
