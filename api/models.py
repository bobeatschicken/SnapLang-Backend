from django.db import models

# Create your models here.


class Images(models.Model):
    english_definition = models.CharField(max_length=255, null=False)
    foreign_definition = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "English definition: {}. Foreign language definition: {}".format(self.english_definition, self.foreign_definition)
