from django.apps import AppConfig


class PerfilAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_app'

    def ready(self):
        import perfil_app.signals

  