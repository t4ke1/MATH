from colorama import init, Fore, Back, Style
import threading
import select
import errno
import time
import builtins

from res.core_func import *

###############################
##                           ##
##        Server core        ##
##                           ##
###############################


# Handling Messages From Clients
def handle(nickname, clients, client):
    while True:
        try:
            # Broadcasting Messages
            message = clients[nickname].recv(1024)
            if nickname not in mutes:
                if get_commad(message, nickname, clients, client) != True:
                    broadcast(message)
            else:
                client.send('<SERVER> Sorry, you muted by the administrator :3'.encode('utf-8'))
        except:
            # Removing And Closing Clients  
            exit(nickname, clients, client)

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(Fore.YELLOW +"[+] Connect try with {}".format(str(address)) + Fore.WHITE)
        # Request And Store Nickname and Version
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        client.send('VER'.encode('utf-8'))
        client_ver = client.recv(1024).decode('utf-8')
        
        
        # Checking Nickname, Ban, Ver
        if nick_check(nickname, client, client_ver, address, ver) != False:
            if ban_check(nickname, client) != True:
                if check_ver(client_ver, ver, client, nickname, address) != False:
                    clients[nickname] = client
                    thread = threading.Thread(target=handle, args=(nickname, clients, client,))
                    thread.start()
                    client.send("[+] Connected to {}!".format(channel_name).encode('utf-8'))
                    broadcast("[+] {} joined!".format(nickname).encode('utf-8'))
                else:
                    client.shutdown(socket.SHUT_RDWR)
                    client.close
            else:
                pass
        else:
            pass