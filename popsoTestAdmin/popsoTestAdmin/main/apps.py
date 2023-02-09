from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'popsoTestAdmin.main'

    def ready(self):
        from .save_data import save
        from .models import ParsedData
        save(ParsedData)

