import socket
import select
import errno
import socket
import threading

print("""
     __    __     ______     ______   __  __    
    /\ "-./  \   /\  __ \   /\__  _\ /\ \_\ \   
    \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \  __ \  
     \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_\ \_\ 
      \/_/  \/_/   \/_/\/_/     \/_/   \/_/\/_/
    -----------------------------------
    Version: Alpha 1_0.6.4
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------
    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!
    -----------------------------------
""")

# Connection Data
host= input('    Set IP: ')
port= int(input('    Set port: '))
channel_name = "#" + input('    Set channel name: ')
ver= 'Alpha 1_0.6.4'

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
            broadcast('[-] {} left the server!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("[+] Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        client_ver = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
       

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        if client_ver == ver:
            print("Client version: " + client_ver)
            broadcast("[+] {} joined!".format(nickname).encode('utf-8'))
            client.send("[+] Connected to {}!".format(channel_name).encode('utf-8'))
        else:
            print("Client version: " + client_ver + " too old!")
            
        # Start Handling Thread For Client
        if client_ver == ver:
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        else:
            clients.remove(client)
            client.close()
            nicknames.remove(nickname)


receive()
