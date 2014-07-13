from django.contrib import admin
from .models import Person, Family, Pet


admin.site.register(Person)
admin.site.register(Family)
admin.site.register(Pet)