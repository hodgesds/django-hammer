class HammerdemoRouter(object):
    """
    A router to control all database operations on models in the
    hammerdemo application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'hammerdemo':
            return 'hammerdemo'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'hammerdemo':
            return 'hammerdemo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'hammerdemo' or \
           obj2._meta.app_label == 'hammerdemo':
           return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the 'hammer'
        database.
        """
        if db == 'hammerdemo':
            return model._meta.app_label == 'hammerdemo'
        elif model._meta.app_label == 'hammerdemo':
            return False
        return None
