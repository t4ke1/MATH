import socket
import select
import errno
import socket
import threading
import os
import time
import sys


print("""
                   :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:  
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!  
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!                      
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!               
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

                                         ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
                                        ▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
                                        ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
                                        ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
                                        ▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
                                        ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
                                        ░  ░      ░  ▒   ▒▒ ░   ░     ▒ ░▒░ ░
                                        ░      ░     ░   ▒    ░       ░  ░░ ░
                                        ░         ░  ░         ░  ░  ░
    """)

time.sleep(2)
os.system('cls||clear')

# Info
print("""
     __    __     ______     ______   __  __    
    /\ "-./  \   /\  __ \   /\__  _\ /\ \_\ \   
    \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \  __ \  
     \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_\ \_\ 
      \/_/  \/_/   \/_/\/_/     \/_/   \/_/\/_/                                    
    -----------------------------------
    Version: Alpha 1_1.0.1 (SERVER CORE)
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------

    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!

    -----------------------------------""")

# Connection Data
try:
    host = input('    Set host IP: ')
    if host == '':
        print("\n    [!]  Please enter IP!")
        time.sleep(5)
        sys.exit() 
except:
    print("\n    [!]  Invalid address format!")
    time.sleep(5)
    sys.exit() 

try:
    port = int(input('    Set host port: '))
except ValueError:
    print("\n    [!]  Port must be an integer!")
    time.sleep(5)
    sys.exit() 
    
channel_name = "#" + input('    Set channel name: ')
ver= 'Alpha 1_1'

print("""
    -----------------------------------""")

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except:
    print("\n    [!]  The given IP or port is busy!")
    time.sleep(5)
    sys.exit() 
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Client Kick Function   
def close_client(client):
    clients.remove(client)
    client.close()

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
            print("[-] {} left the server!".format(nickname))
            print("""    -----------------------------------""")
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
        clients.append(client)
       
        # Checking Nickname
        if nickname in nicknames:
            print("    Nickname is {}".format(nickname) +" (ALREADY EXISTS!)")
            # If Old - Kick Him
            if client in clients:
                client.send("[-] You have been kicked from the server! Code 401".encode('utf-8'))
                close_client(client)
            check_ver(client_ver, ver, client, clients, nickname, address)
            broadcast('[!] {} try to connect again... Already exist!'.format(nickname).encode('utf-8'))
            print("[!] {} {} kicked from the server! Already exist.".format(nickname, str(address)))
            print("""    -----------------------------------""")
        else:
            print("    Nickname is {}".format(nickname))
            nicknames.append(nickname)
            is_normal = check_ver(client_ver, ver, client, clients, nickname, address)
            if is_normal == True:
                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
                client.send("[+] Connected to {}!".format(channel_name).encode('utf-8'))
                broadcast("[+] {} joined!".format(nickname).encode('utf-8'))    
            
# Checking Version Function
def check_ver(client_ver, ver, client, clients, nickname, address):
        if client_ver == ver:
            # If All Is Good - Go Next
            print("    Client version: " + client_ver)
            print("""    -----------------------------------""")
            return True
        else:
            print("    Client version: " + client_ver + " (TOO OLD!)")
            print("""    -----------------------------------""")
            # If Old - Kick Him
            if client in clients:
                print("[-] {} {} kicked from the server! Too old version.".format(nickname, str(address)))
                client.send("[-] You have been kicked from the server! Code 409".encode('utf-8'))
                close_client(client)
                broadcast('[-] {} kicked from the server! Too old version.'.format(nickname).encode('utf-8'))
                print("""    -----------------------------------""")
            nicknames.remove(nickname)
            return False

#Start Listening
receive()


