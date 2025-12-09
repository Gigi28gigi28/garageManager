from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "service"
    
    def ready(self):
        import pika
        with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as con:
            ch=con.channel()
            ch.queue_declare(queue="garage",durable=True)
        return super().ready()
