from django.apps import AppConfig


class LandingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Landing'
    # Starts signals to create author profile.
    def ready(self):
        from . import signals
