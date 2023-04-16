from django.db import models

# Create your models here.


class jsondata(models.Model):
    end_year=models.CharField(max_length=100, blank=True, null=True)
    intensity=models.IntegerField()
    sector=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    insight=models.CharField(max_length=100)
    url=models.URLField()
    region=models.CharField(max_length=100)
    start_year=models.CharField(max_length=100, blank=True, null=True)
    impact=models.CharField(max_length=100, blank=True, null=True)
    country=models.CharField(max_length=100)
    relevance=models.IntegerField()
    pestle=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    likelihood=models.IntegerField()

    def __str__(self):
        return self.sector

    # add more fields as necessary
