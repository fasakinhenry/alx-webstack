from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'serviceproviders'


    def ready(self):
        import serviceproviders.signals
