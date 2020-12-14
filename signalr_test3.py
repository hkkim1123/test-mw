from signalrcore.hub_connection import HubConnection

server_url = "ws://localhost:62342/chathub"
username = "mandrewcito"

hub_connection = HubConnection(server_url)
hub_connection.build()
hub_connection.on("ReceiveMessage", print)
hub_connection.start()
message = None
# Do login

while message != "exit()":
    message = input(">> ")
    if message is not None and message is not "" and message is not "exit()":
        hub_connection.send("SendMessage", [username, message])
hub_connection.stop()