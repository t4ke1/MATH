import socket
import select
import errno
from colorama import init, Fore, Back, Style
import socket
import threading
import os
import time
import sys

init(convert=True)

print(Fore.CYAN +"""
                                _
                             ,:'/   _..._
                            // ( `""-.._.'
                            \| /    6\___
                            |     6      4
                            |            /
                            \_       .--'
                            (_'---'`)
                            / `'---`()
                          ,'        |
         ,            .'`          |
         )\       _.-'             ;
        / |    .'`   _            /
       /` /   .'       '.        , |
      /  /   /           \   ;   | |
      |  \  |            |  .|   | |
       \  `"|           /.-' |   | |
        '-..-\       _.;.._  |   |.;-.
              \    <`.._  )) |  .;-. ))
              (__.  `  ))-'  \_    ))'
                  `'--"`       `--"
                  
    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ██╔████╔██║███████║   ██║   ███████║
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝  Ampernic`s fork (Psinamper server core)""" + Fore.WHITE)

time.sleep(2)
os.system('cls||clear')

print(Fore.CYAN + """
    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ██╔████╔██║███████║   ██║   ███████║
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
""" + "\33[90m" + """
    -----------------------------------""" + Fore.CYAN + """
    Version: Alpha 1_1
    Author: Wiskey666
    Forked by: Ampernic
    Mail: ampernic@list.ru
    DS: ampernic#9787""" + "\33[90m" + """
    -----------------------------------""" + Fore.CYAN + """

    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!
""" + "\33[90m" + """
    -----------------------------------""" + Fore.CYAN + """
    """+ Fore.WHITE)

# Init
try:
    config = open('main.conf')
    config.readline()
    auto = int(config.readline().rstrip()[6:])
    log = int(config.readline().rstrip()[5:])

    if auto == 1:
        host = config.readline().rstrip()[4:]
        print("    Auto-init host: " + host)
        port = int(config.readline().rstrip()[6:])
        print("    Auto-init port: " + str(port))
        channel_name = config.readline().rstrip()[9:]
        print("    Auto-init channel name: " + channel_name)
            
    else:
        try:
            host = input('    Set host IP: ')
            if host == '':
                print(Fore.YELLOW + "\n    [!]  Please enter IP!")
                time.sleep(5)
                sys.exit() 
        except:
            print(Fore.YELLOW + "\n    [!]  Invalid address format!")
            time.sleep(5)
            sys.exit() 

        try:
            port = int(input('    Set host port: '))
        except ValueError:
            print(Fore.YELLOW + "\n    [!]  Port must be an integer!")
            time.sleep(5)
            sys.exit() 
            
        channel_name = "#" + input('    Set channel name: ')
except:
    print(Fore.YELLOW + "\n    [!]  Сonfig does not exist or has an invalid format!")
    time.sleep(5)
    sys.exit() 

<<<<<<< Updated upstream
try:
    port = int(input('    Set host port: '))
except ValueError:
    print(Fore.YELLOW + "\n    [!]  Port must be an integer!")
    time.sleep(5)
    sys.exit() 
    
channel_name = "#" + input('    Set channel name: ')
ver= 'Alpha 1_1'
=======
rules = config.readline().rstrip()[7:]

ver= 'Alpha 1_2.5.1'
>>>>>>> Stashed changes

print("\33[90m" + """
    -----------------------------------"""+ Fore.WHITE)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except:
    print(Fore.YELLOW + "\n    [!]  The given IP or port is busy!")
    time.sleep(5)
    sys.exit() 
    
server.listen()

# Dictionary For Clients and Their Nicknames
clients = {}

# Sending Messages To All Connected Clients
def broadcast(message):
    for x in clients:
        clients[x].send(message)

# Client Close Function   
def user_exit(nickname, clients, client):
    if nickname in clients:
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        client.close
        del clients[nickname]
        broadcast('[-] {} left the server!'.format(nickname).encode('utf-8'))
        print(Fore.YELLOW + "[-] {} left the server!".format(nickname))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
    
# Getting Command Function
def get_commad(message, nickname, clients, client):
    message_text = message.decode('utf-8')
    nickcount = len('<' + nickname + '> ')
    message_text = message_text[nickcount:]
    
    print(message_text)

    if "/kick" in message_text:
        if message_text[6:] in clients:
            broadcast('[-] {} kicked from the server by {}!'.format(message_text[6:], nickname).encode('utf-8'))
            clients[message_text[6:]].send("[-] You have been kicked from the server by {}! Code 400".format(nickname).encode('utf-8'))
            print(Fore.YELLOW + "[-] {} kicked from the server by {}!".format(message_text[6:], nickname))
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            print(clients[message_text[6:]])
            clients[message_text[6:]].close()
            del clients[message_text[6:]]
        else:
            print('Name: '+ message_text[6:]+ '(NOT EXIST)')
    elif "/rules" in message_text:
        clients[nickname].send(rules.encode('utf-8'))
    elif "/q" in message_text:
        user_exit(nickname, clients, client)

# Handling Messages From Clients
def handle(nickname, clients, client):
    while True:
        try:
            # Broadcasting Messages
            sl = client
            message = client.recv(1024)
            broadcast(message)
            get_commad(message, nickname, clients, client)
        except:
            # Removing And Closing Clients  
            user_exit(nickname, clients, client)

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(Fore.YELLOW +"[+] Connected with {}".format(str(address)) + Fore.WHITE)

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        client_ver = client.recv(1024).decode('utf-8')
        
        # Checking Nickname
        if nickname in clients:
            print("    Nickname is {}".format(nickname) + Fore.RED + " (ALREADY EXISTS!)" + Fore.WHITE)
            client.send("[-] You have been kicked from the server! Code 401".encode('utf-8'))
            check_ver(client_ver, ver, client, clients, nickname, address)
            broadcast('[!] {} try to connect again... Already exist!'.format(nickname).encode('utf-8'))
            print(Fore.YELLOW + "[!] {} {} kicked from the server! Already exist.".format(nickname, str(address)) + Fore.WHITE)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        else:
            print("    Nickname is {}".format(nickname))
            clients[nickname] = client
            is_normal = check_ver(client_ver, ver, client, clients, nickname, address)
            if is_normal == True:
                thread = threading.Thread(target=handle, args=(nickname, clients, client,))
                thread.start()
                client.send("[+] Connected to {}!".format(channel_name).encode('utf-8'))
                broadcast("[+] {} joined!".format(nickname).encode('utf-8'))    
            
# Checking Version Function
def check_ver(client_ver, ver, client, clients, nickname, address):
        if client_ver == ver:
            # If All Is Good - Go Next
            print("    Client version: " + client_ver)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            return True
        else:
            print("    Client version: " + client_ver + Fore.RED + " (UNSUPPORTED!)" + Fore.WHITE)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            # If Old - Kick Him
            if client == clients[nickname]:
                print(Fore.YELLOW + "[-] {} {} kicked from the server! Unsupported version.".format(nickname, str(address)) + Fore.WHITE)
                client.send("[-] You have been kicked from the server! Code 409".encode('utf-8'))
                client.close
                broadcast('[-] {} kicked from the server! Too old version.'.format(nickname).encode('utf-8'))
                print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            return False

#Start Listening
receive()


