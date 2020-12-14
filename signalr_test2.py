import logging

from signalrcore.hub_connection_builder import HubConnectionBuilder

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# HubConnectionBuilder.hub = 'ESLNotificationHub'
notification = HubConnectionBuilder()\
    .with_url('http://os3.prestige.de:8080/?version=1&serial=1349001533&store=4', options={
        "verify_ssl": False,
        "headers": {
    }})\
    .configure_logging(logging.DEBUG, socket_trace=True, handler=handler)\
    .with_automatic_reconnect({
        "type": "interval",
        "keep_alive_interval": 10,
        "intervals": [1, 3, 5, 6, 7, 87, 3]
    })\
    .build()

notification.on_open(lambda: print("connection opened and handshake received ready to send messages"))
notification.on_close(lambda: print("connection closed"))
notification.on_error(lambda: print("notification error"))
notification.start()
# notification.stop()
