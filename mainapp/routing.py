from django.urls import path
from . import consumers
websocket_urlpatterns =[
    path('ws/stock/<str:room_name>/', consumers.StockConsumer.as_asgi()),
]