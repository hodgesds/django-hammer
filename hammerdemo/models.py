from django.db import models
from django.core.urlresolvers import reverse


class DemoPersonSiblings(models.Model):
    class Meta:
        db_table = 'demo_person_siblings'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    from_person_id = models.IntegerField(db_column='from_person_id', null=False, blank=False, primary_key=False, max_length=4)
    to_person_id = models.IntegerField(db_column='to_person_id', null=False, blank=False, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demopersonsiblings_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoPerson(models.Model):
    class Meta:
        db_table = 'demo_person'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    sex = models.SmallIntegerField(db_column='sex', null=False, blank=False, primary_key=False, max_length=2)
    first = models.CharField(db_column='first', null=False, blank=False, primary_key=False, max_length=60)
    last = models.CharField(db_column='last', null=False, blank=False, primary_key=False, max_length=60)
    age = models.SmallIntegerField(db_column='age', null=False, blank=False, primary_key=False, max_length=2)
    alive = models.BooleanField(db_column='alive', null=False, blank=False, primary_key=False, default=True)
    spouse_id = models.IntegerField(db_column='spouse_id', null=True, blank=True, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demoperson_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoPersonParents(models.Model):
    class Meta:
        db_table = 'demo_person_parents'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    from_person_id = models.IntegerField(db_column='from_person_id', null=False, blank=False, primary_key=False, max_length=4)
    to_person_id = models.IntegerField(db_column='to_person_id', null=False, blank=False, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demopersonparents_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoFamilyPets(models.Model):
    class Meta:
        db_table = 'demo_family_pets'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    family_id = models.IntegerField(db_column='family_id', null=False, blank=False, primary_key=False, max_length=4)
    pet_id = models.IntegerField(db_column='pet_id', null=False, blank=False, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demofamilypets_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoFamily(models.Model):
    class Meta:
        db_table = 'demo_family'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    name = models.CharField(db_column='name', null=False, blank=False, primary_key=False, max_length=60)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demofamily_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoFamilyMembers(models.Model):
    class Meta:
        db_table = 'demo_family_members'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    family_id = models.IntegerField(db_column='family_id', null=False, blank=False, primary_key=False, max_length=4)
    person_id = models.IntegerField(db_column='person_id', null=False, blank=False, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demofamilymembers_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoPet(models.Model):
    class Meta:
        db_table = 'demo_pet'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    sex = models.SmallIntegerField(db_column='sex', null=False, blank=False, primary_key=False, max_length=2)
    owner_id = models.IntegerField(db_column='owner_id', null=True, blank=True, primary_key=False, max_length=4)
    name = models.CharField(db_column='name', null=False, blank=False, primary_key=False, max_length=60)
    age = models.SmallIntegerField(db_column='age', null=False, blank=False, primary_key=False, max_length=2)
    species = models.CharField(db_column='species', null=False, blank=False, primary_key=False, max_length=60)
    alive = models.BooleanField(db_column='alive', null=False, blank=False, primary_key=False, default=True)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demopet_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


class DemoPersonChildren(models.Model):
    class Meta:
        db_table = 'demo_person_children'
        managed=False
    id = models.IntegerField(db_column='id', null=False, blank=False, primary_key=True, max_length=4)
    from_person_id = models.IntegerField(db_column='from_person_id', null=False, blank=False, primary_key=False, max_length=4)
    to_person_id = models.IntegerField(db_column='to_person_id', null=False, blank=False, primary_key=False, max_length=4)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('demopersonchildren_detail', kwargs={'pk': self.pk})

    @property
    def tuple_vals(self):
        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)


