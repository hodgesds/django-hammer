from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db import connections
from django.conf import settings
from utils.hammer import Hammer

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
        apps = settings.INSTALLED_APPS
        additional_settings = ''
        additional_urls = ''
        for con in connections.all():
            db_name = con.settings_dict.get('NAME')
            hammer_db = con.settings_dict.get('HAMMER')
            if hammer_db:
                print 'Setting up database "{0}"'.format(db_name)
                cur = con.cursor()
                data_types_dict = cur.db.introspection.data_types_reverse
                tables = cur.db.introspection.get_table_list(cur)
                table_dict = {x:{} for x in tables}
                installed_models = cur.db.introspection.installed_models(cur)
                for t in tables:
                    print 'Introspecting table "{0}"'.format(t)
                    table_dict[t]['converted_name'] = cur.db.introspection.table_name_converter(t)
                    table_dict[t]['django_name'] = cur.db.introspection.django_table_names(t)
                    table_dict[t]['table_spec'] = cur.db.introspection.get_table_description(cur, t)
                    table_dict[t]['constraints'] = cur.db.introspection.get_constraints(cur, t)
                    table_dict[t]['relations'] = cur.db.introspection.get_relations(cur, t)
                    table_dict[t]['pk'] = cur.db.introspection.get_primary_key_column(cur, t)
                    table_dict[t]['key_columns'] = cur.db.introspection.get_key_columns(cur, t)
                hammer = Hammer(data_types=data_types_dict, models=table_dict, app_name=con.alias, app_db=con.settings_dict)
                additional_settings += hammer.setup()
                additional_urls += "    url(r'^%s/', include('%s.urls'))," % (con.alias, con.alias)
        if len(additional_settings) > 0:
            print "\n\nAdd the following lines to (the end of) settings.py\n\n{0}\n".format(''.join(additional_settings))
        if len(additional_urls) > 0:
            print "\nAdd the following lines to urls.py\n\n{0}\n".format(''.join(additional_urls))