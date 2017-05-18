from django.db import models
from district.models import District
from institute.models import Institute
# Create your models here.


class Student(models.Model):
    std_id = models.IntegerField(primary_key = True)
    std_name = models.CharField(max_length = 200)
    dist_id = models.ForeignKey(District)
    ins_id = models.ForeignKey(Institute)
    std_phone = models.CharField(max_length = 15, unique = True)
    std_admission = models.DateField()

    def __str__(self):
        return self.std_id + ". " + self.std_name
