from django.db import models
from district.models import District

# Create your models here.


class Institute(models.Model):
    ins_id = models.IntegerField(primary_key = True)
    ins_name = models.CharField(max_length = 200, unique = True)
    dist_id = models.ForeignKey(District)

    def __str__(self):
        return self.ins_id + ". " + self.ins_name