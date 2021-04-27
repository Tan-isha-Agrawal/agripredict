from django.db import models


class PredResults2(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.FloatField()
    Fertilizers = models.FloatField()
    Rainfall = models.FloatField()
    Storage = models.FloatField()
    Electricity = models.FloatField()
    yeild = models.FloatField()
    prices = models.FloatField()

    def __str__(self):
        return self.id
