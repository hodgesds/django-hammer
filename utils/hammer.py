from django.conf import settings
from django.template import Context, Template
from django.template.loader import render_to_string, get_template
import os

def lcu_to_cc(string):
    """Convert string or unicode from lower-case underscore to camel-case"""
    splitted_string = string.split('_')
    return str(splitted_string[0].title()) + ''.join([x.title() for x in map(str, splitted_string[1:])])


class Hammer(object):
    def __init__(self, mode='crud', path=settings.BASE_DIR, app_name='api', admin=True, data_types={}, urls=True,\
                 models=True, api_format=['json'], app_db=None, test=True):
        self.settings = ''
        self.url_settings = ''
        self.mode = mode
        self.app_name = app_name
        self.models = models
        self.urls = urls
        self.admin = admin
        self.test = test
        self.api_format = api_format
        self.path = path
        self.app_dir = self.path + '/' + self.app_name
        self.data_types = data_types
        self.db = app_db

    def setup(self):
        self.create_app_dir()
        if self.urls:
            self.create_urls_file()
        if self.admin:
            self.create_admin_file()
        if self.models:
            self.create_models_file()
            self.create_views_file()
            self.create_template_files()
            self.create_view_tests()
        self.add_api_router()
        return self.settings

    def create_app_dir(self):
        if not os.path.exists(self.path + '/' + self.app_name):
            print "Creating application directory:\n{0}".format(self.app_dir)
            os.mkdir(self.app_dir)
        if not os.path.exists(self.path + '/' + self.app_name + '/__init__.py'):
            initr = self.path + '/' + self.app_name + '/__init__.py'
            open(initr, 'a').close()
        if not os.path.exists(self.path + '/' + self.app_name + '/templates'):
            os.mkdir(self.path + '/' + self.app_name + '/templates')
        self.settings += "INSTALLED_APPS += ('{0}',)\n".format(self.app_name)

    def create_file(self, name, data):
        with open(name, 'w') as f:
            for line in data:
                try:
                    f.write(line+'\n')
                except IOError:
                    print 'Error writing line:\n {0}'.format(line)

    def create_model_test_data(self, model):
        if model.get('converted_name') and not model.get('django_name'):
            model_name = lcu_to_cc(model.get('converted_name'))
            spec = model.get('table_spec')
            data = []
            for col in spec:
                code = col.type_code
                field_null = col.null_ok
                field = self.data_types.get(code)
                if 'Boolean' in field:
                    default = True
                if field in ('CharField','CommaSeparatedIntegerField','FileField','FilePathField','ImageField',):
                    data.append("{} = 'test'".format(col.name))
                elif field in ('EmailField'):
                    data.append("{} = 'test@test.com'".format(col.name))
                elif 'Boolean' in field and not field_null:
                    data.append("{} = True".format(col.name))
                else:
                    data.append("{} = 1".format(col.name))
            return data
        return None

    def create_model_doctest(self, model):
        if model.get('converted_name') and not model.get('django_name'):
            model_name = lcu_to_cc(model.get('converted_name'))
            spec = model.get('table_spec')
            data = []
            field_list = []
            for col in spec:
                field_null = col.null_ok
                code = col.type_code
                field = self.data_types.get(code)
                size = col.internal_size
                pk =  col.name == model.get('pk')
                if 'Boolean' in field:
                    default = True
                if field in ('CharField','CommaSeparatedIntegerField','FileField','FilePathField','ImageField',):
                    data.append("{} = 'test'".format(col.name))
                    field_list.append((col.name, 'test'))
                elif field in ('EmailField'):
                    data.append("{} = 'test@test.com'".format(col.name))
                    field_list.append((col.name, 'test@test.com'))
                elif 'Boolean' in field and not field_null:
                    data.append("{} = True".format(col.name))
                    field_list.append((col.name, 'True'))
                else:
                    data.append("{} =1".format(col.name))
                    field_list.append((col.name, '1'))
        tvals = "("
        for f in field_list:
            if isinstance(f[1], unicode):
                tvals += "('{0}', u'{1}'), ".format(f[0], f[1])
            elif isinstance(f[1], basestring):
                tvals += "('{0}', '{1}'), ".format(f[0], f[1])
            else:
                tvals += "('{0}', {1}), ".format(f[0], f[1])
        tvals += ")"
        res = "    \"\"\"\n    >>> {0}.objects.create({1}).__unicode__() == '1'".format(model_name,', '.join(data))
        res += "\n    True\n    \"\"\"".format(model_name, tvals)
        return res

    def create_models_file(self):
        file_name = self.app_dir + '/models.py'
        print "Setting up models.py in file:\n{0}".format(file_name)
        data = ['from django.db import models','from django.core.urlresolvers import reverse','','']
        for key, model in self.models.items():
            if model.get('converted_name') and not model.get('django_name'):
                model_name = 'class {0}(models.Model):'.format(lcu_to_cc(model.get('converted_name')))
                abs_url = "reverse('%s_detail', kwargs={'pk': self.pk})" % (model.get('converted_name').replace('_',''),)
                data.append(model_name)
                data.append('    class Meta:') # add in meta info
                data.append("        db_table = '{0}'".format(model.get('converted_name')))
                data.append("        managed=False")
                spec = model.get('table_spec')
                for col in spec:
                    field_null = col.null_ok
                    code = col.type_code
                    field = self.data_types.get(code)
                    size = col.internal_size
                    pk =  col.name == model.get('pk')
                    if 'Boolean' in field:
                        default = True
                    if field in ('CharField','CommaSeparatedIntegerField','EmailField','FileField','FilePathField','ImageField',):
                        data.append("    {1} = models.{0}(db_column='{1}', null={2}, blank={2}, primary_key={3}, max_length={4})".format(
                            field,
                            col.name,
                            field_null,
                            pk,
                            size,
                        ))
                    elif 'Boolean' in field and not field_null:
                        data.append("    {1} = models.{0}(db_column='{1}', null={2}, blank={2}, primary_key={3}, default={4})".format(
                            field,
                            col.name,
                            field_null,
                            pk,
                            default,
                        ))
                    else:
                        data.append("    {1} = models.{0}(db_column='{1}', null={2}, blank={2}, primary_key={3}, max_length={4})".format(
                            field,
                            col.name,
                            field_null,
                            pk,
                            size,
                        ))
                data += ['','    def __unicode__(self):','        return str(self.pk)']
                data += ['','    def get_absolute_url(self):']
                data += ["        return " + abs_url]
                data += ['','    @property','    def tuple_vals(self):', '        return tuple((x.name, getattr(self, x.name),) for x in self._meta.fields)']
                data += ['', '']
        self.create_file(file_name, data)


    def create_admin_file(self):
        file_name = self.app_dir + '/admin.py'
        print "Setting up admin.py in file:\n{0}".format(file_name)
        app_models = [lcu_to_cc(x) for x in self.models.keys()]
        context = Context({'app':self.app_name, 'app_db':self.db.get('NAME'), 'app_models':app_models})
        template = get_template('admin.txt')
        rendered_template = template.render(context)
        self.create_file(file_name, rendered_template.split('\n'))


    def create_urls_file(self):
        file_name = self.app_dir + '/urls.py'
        print "Creating urls.py in file:\n{0}".format(file_name)
        app_models = [lcu_to_cc(x) for x in self.models.keys()]
        context = Context({'app':self.app_name, 'app_db':self.db.get('NAME'), 'app_models':app_models})
        template = get_template('urls.txt')
        rendered_template = template.render(context)
        self.create_file(file_name, rendered_template.split('\n'))


    def create_views_file(self):
        file_name = self.app_dir + '/views.py'
        print "Creating views.py in file:\n{0}".format(file_name)
        app_models = [lcu_to_cc(x) for x in self.models.keys()]
        context = Context({'app':self.app_name, 'app_db':self.db.get('NAME'), 'app_models':app_models})
        template = get_template('views.txt')
        rendered_template = template.render(context)
        self.create_file(file_name, rendered_template.split('\n'))


    def create_template_files(self):
        for key, model in self.models.items():
            model_name = model.get('converted_name')
            # make detail template
            file_name = self.app_dir + '/templates/' + model_name.replace('_', '') + '_detail.html'
            template_string = "{% block body %} <ul> {% for field in object.tuple_vals %} <li><b>{{ field.0 }}:</b> {{ field.1 }}</li> {% endfor %} </ul> {% endblock %}"
            self.create_file(file_name, [template_string])
            print 'Creating template "{0}" for model {1}'.format(file_name, model_name)
            # make the list template
            file_name = self.app_dir + '/templates/' + model_name.replace('_', '') + '_list.html'
            template_string = "{% block body %} <table> {% for object in object_list %} {% if forloop.first %} <tr> {% for field in object.tuple_vals %} <td>{{field.0}}</td> {% endfor %} </tr> {% endif %} <tr> {% for field in object.tuple_vals %} <td>{{field.1}} </td> {% endfor %} </tr> {% endfor %} </table> {% endblock %}"
            self.create_file(file_name, [template_string])
            print 'Creating template "{0}" for model {1}'.format(file_name, model_name)
            # make the create template
            file_name = self.app_dir + '/templates/' + model_name.replace('_', '') + '_confirm_delete.html'
            template_string = '<form action="" method="post">{% csrf_token %} <p>Are you sure you want to delete "{{ object }}"?</p> <input type="submit" value="Confirm" /> </form>'
            self.create_file(file_name, [template_string])
            print 'Creating template "{0}" for model {1}'.format(file_name, model_name)
            file_name = self.app_dir + '/templates/' + model_name.replace('_', '') + '_create.html'
            template_string = '<form action="" method="post">{% csrf_token %} {{form}}<br> <input type="submit" value="Confirm" /> </form>'
            self.create_file(file_name, [template_string])
            print 'Creating template "{0}" for model {1}'.format(file_name, model_name)


    def create_view_tests(self):
        file_name = self.app_dir + '/tests.py'
        print "Creating tests.py in file:\n{0}".format(file_name)
        app_models = [lcu_to_cc(x) for x in self.models.keys()]
        model_data = [[', '.join(self.create_model_test_data(model)), lcu_to_cc(name)] for name, model in self.models.items()]
        context = Context({'app':self.app_name, 'app_db':self.db.get('NAME'), 'app_models':app_models, 'model_data':model_data})
        template = get_template('tests.txt')
        rendered_template = template.render(context)
        self.create_file(file_name, rendered_template.split('\n'))
        return True

    def add_read_view(self, model):
        return True

    def add_create_view(self, model):
        return True

    def add_update_view(self, model):
        return True

    def add_delete_view(self, model):
        return True

    def add_api_router(self):
        context = Context({'app':self.app_name, 'app_db':self.db.get('NAME')})
        template = get_template('router.txt')
        rendered_template = template.render(context)
        file_name = self.app_dir + '/router.py'
        self.create_file(file_name, rendered_template.split('\n'))
        self.settings += "DATABASE_ROUTERS += ['{0}.{1}.{2}']".format(self.app_name, 'router', self.app_name.title()+'Router')
        print 'Adding database routing settings in file:\n{0}'.format(file_name)
