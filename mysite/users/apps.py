from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

#Django invokes the ready() method of each app's AppConfig class when the application is fully loaded and ready for use.
#The primary purpose of the ready() method is to provide a convenient place to register signals, set up event listeners, or perform any other initialization tasks specific to your app. 
    def ready(self): #
        import users.signals #  you import the signals module(users.signals), which contains the definitions for your custom signals.