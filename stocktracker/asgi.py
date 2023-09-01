import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import mainapp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocktracker.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        mainapp.routing.websocket_urlpatterns 
        
    )
    
})