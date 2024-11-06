from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Measurement(models.Model):

    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements'
        )
    temperature = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
