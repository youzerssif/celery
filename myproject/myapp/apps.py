from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    def ready(self):
        from .auto import update
        update.start()