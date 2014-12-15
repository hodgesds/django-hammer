from django.contrib import admin
from hammerdemo.models import (
    
    DemoPersonSiblings,
    
    DemoPerson,
    
    DemoPersonParents,
    
    DemoFamilyPets,
    
    DemoFamily,
    
    DemoFamilyMembers,
    
    DemoPet,
    
    DemoPersonChildren,
    
)

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'hammerdemo'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'hammerdemo' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'hammerdemo' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'hammerdemo' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'hammerdemo' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'hammer' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)



admin.site.register(DemoPersonSiblings, MultiDBModelAdmin)

admin.site.register(DemoPerson, MultiDBModelAdmin)

admin.site.register(DemoPersonParents, MultiDBModelAdmin)

admin.site.register(DemoFamilyPets, MultiDBModelAdmin)

admin.site.register(DemoFamily, MultiDBModelAdmin)

admin.site.register(DemoFamilyMembers, MultiDBModelAdmin)

admin.site.register(DemoPet, MultiDBModelAdmin)

admin.site.register(DemoPersonChildren, MultiDBModelAdmin)

