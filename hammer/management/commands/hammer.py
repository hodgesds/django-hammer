from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db import connections
from django.conf import settings

class Command(BaseCommand):
    help = "Hammers out an API from db tables"
    dbs = connections.databases
    option_list = BaseCommand.option_list + (
        make_option('--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force model creation'),
        )
    def handle(self, *args, **options):
        print args, options
        apps = settings.INSTALLED_APPS
        for con in connections.all():
            db_name = con.settings_dict['NAME']
            print 'Setting up database {0}'.format(db_name)
            cur = con.cursor()
            data_types_dict = cur.db.introspection.data_types_reverse
            tables = cur.db.introspection.get_table_list(cur)
            table_dict = {x:{} for x in tables}
            installed_models = cur.db.introspection.installed_models(cur)
            print 'Found tables:\n {0}'.format(', '.join(tables))
            for t in tables:
                table_dict[t]['converted_name'] = cur.db.introspection.table_name_converter(t)
                table_dict[t]['django_name'] = cur.db.introspection.django_table_names(t)
                table_dict[t]['desc'] = cur.db.introspection.get_table_description(cur, t)
                table_dict[t]['table_spec'] = cur.db.introspection.get_table_description(cur, t)
                table_dict[t]['constraints'] = cur.db.introspection.get_constraints(cur, t)
                table_dict[t]['relations'] = cur.db.introspection.get_relations(cur, t)


