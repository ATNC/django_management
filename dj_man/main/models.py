from django.db import models

class People(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s"%(self.name)


class Document(models.Model):
    education = models.CharField(max_length=255, unique=True)
    people = models.ManyToManyField(People)

    def __unicode__(self):
        return "%s"%(self.education)
