from django.db import models

sexes = ((1, "Male"), (2, "Female"), (3, "Other"))
class Person(models.Model):
    sex = models.PositiveSmallIntegerField(choices=sexes)
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    alive = models.BooleanField(default=True)
    spouse = models.ForeignKey('Person', null=True, blank=True)
    parents = models.ManyToManyField('Person', related_name='person_parents', null=True, blank=True)
    siblings = models.ManyToManyField('Person', related_name='person_siblings', null=True, blank=True)
    children = models.ManyToManyField('Person', related_name='person_children', null=True, blank=True)

    def __unicode__(self):
        return self.first + ' ' + self.last

class Family(models.Model):
    name = models.CharField(max_length=60)
    members = models.ManyToManyField(Person)
    pets = models.ManyToManyField('Pet', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Pet(models.Model):
    sex = models.PositiveSmallIntegerField(choices=sexes)
    owner = models.ForeignKey(Person, null=True, blank=True)
    name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    species = models.CharField(max_length=60)
    alive = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name