from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    '''signals.py should be registered in apps.py, like this'''
    def ready(self):
    	import users.signals
