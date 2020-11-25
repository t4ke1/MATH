import socket
import select
import errno
from colorama import init, Fore, Back, Style
import socket
import threading

init(convert=True)

print("\033[36m" + """
    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ██╔████╔██║███████║   ██║   ███████║
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

    -----------------------------------
    Version: Alpha 1_0.2
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------

    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!

    -----------------------------------
""")
print(Style.RESET_ALL)

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('[-] {} left the server!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("[+] Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("[+] {} joined!".format(nickname).encode('ascii'))
        client.send('[+] Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
