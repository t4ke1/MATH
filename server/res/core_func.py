from colorama import init, Fore, Back, Style
import socket

###############################
##                           ##
##        Secure core        ##
##                           ##
###############################

# Nickname Check Function
def nick_check(nickname, client, client_ver, address, ver):
    if nickname not in clients:
        if " " in nickname:
            print("    Nickname is {}".format(nickname) + Fore.RED + " (INCORRECT!)" + Fore.WHITE)
            client.send("[-] You have been kicked from the server! Code 503".encode('utf-8'))
            check_ver(client_ver, ver, client, nickname, address)
            print(Fore.YELLOW + "[!] {} {} kicked from the server! Incorrect nickname.".format(nickname, str(address)) + Fore.WHITE)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            return False
        elif len(nickname) > 10:
            print("    Nickname is {}".format(nickname) + Fore.RED + " (INCORRECT!)" + Fore.WHITE)
            client.send("[-] You have been kicked from the server! Code 503".encode('utf-8'))
            check_ver(client_ver, ver, client, nickname, address)
            print(Fore.YELLOW + "[!] {} {} kicked from the server! Incorrect nickname.".format(nickname, str(address)) + Fore.WHITE)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            return False
        elif len(nickname) < 3:
            print("    Nickname is {}".format(nickname) + Fore.RED + " (INCORRECT!)" + Fore.WHITE)
            client.send("[-] You have been kicked from the server! Code 503".encode('utf-8'))
            check_ver(client_ver, ver, client, nickname, address)
            print(Fore.YELLOW + "[!] {} {} kicked from the server! Incorrect nickname.".format(nickname, str(address)) + Fore.WHITE)
            print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
            return False
        else:
            print("    Nickname is {}".format(nickname))
            return True
    else:
        print("    Nickname is {}".format(nickname) + Fore.RED + " (ALREADY EXISTS!)" + Fore.WHITE)
        client.send("[-] You have been kicked from the server! Code 401".encode('utf-8'))
        check_ver(client_ver, ver, client, nickname, address)
        broadcast('[!] {} try to connect again... Already exist!'.format(nickname).encode('utf-8'))
        print(Fore.YELLOW + "[!] {} {} kicked from the server! Already exist.".format(nickname, str(address)) + Fore.WHITE)
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)

# Checking Version Function
def check_ver(client_ver, ver, client, nickname, address):
    if client_ver == ver:
        # If All Is Good - Go Next
        print("    Client version: " + client_ver)
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        return True
    else:
        print("    Client version: " + client_ver + Fore.RED + " (UNSUPPORTED!)" + Fore.WHITE)
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        # If Old - Kick Him
        print(Fore.YELLOW + "[-] {} {} kicked from the server! Unsupported version.".format(nickname, str(address)) + Fore.WHITE)
        client.send("[-] You have been kicked from the server! Code 409".encode('utf-8'))
        client.close
        broadcast('[-] {} {} kicked from the server! Unsupported version.'.format(nickname, str(address)).encode('utf-8'))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        return False

# Checking For Ban Function
def ban_check(nickname, client):
    if nickname in bans:
        print(Fore.YELLOW + "[-] {} try to connect but... banned on the server!".format(nickname) + Fore.WHITE)
        client.send("[-] You have been banned on the server! Code 403".encode('utf-8'))
        client.shutdown(socket.SHUT_RDWR)
        client.close
        broadcast('[-] {} try connect. Banned on the server!'.format(nickname).encode('utf-8'))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        return True

###############################
##                           ##
##       Command core        ##
##                           ##
###############################

######################################
#            Mute core               #
######################################

def mute(nickname, admin):
    if nickname in clients:
        if nickname in mutes:
            clients[admin].send("Sorry, but {} already muted.".format(nickname).encode('utf-8'))
        else:
            mutes.append(nickname)
            clients[admin].send("<SERVER> {} successfully muted.".format(nickname).encode('utf-8'))
            clients[nickname].send("You has been muted by {}".format(admin).encode('utf-8'))
    else:
        clients[admin].send("<SERVER> Sorry, but {} not found.".format(nickname).encode('utf-8'))
        
def unmute(nickname, admin):
    if nickname in mutes:
        mutes.remove(nickname)
        clients[admin].send("<SERVER> {} successfully unmuted.".format(nickname).encode('utf-8'))
        clients[nickname].send("You has been unmuted by {}.".format(admin).encode('utf-8'))
    else:
        clients[admin].send("<SERVER> Sorry, but {} already unmuted or not muted.".format(nickname).encode('utf-8'))
        
######################################
#           Ban/kick core            #
######################################

def kick(nickname, admin):
    if nickname in clients:
        # Send Info
        clients[nickname].send("[-] You have been kicked from the server by {}! Code 400".format(admin).encode('utf-8'))
        clients[admin].send("<SERVER> {} successfully kicked.".format(nickname).encode('utf-8'))
        broadcast('[-] {} kicked from the server by {}!'.format(nickname, admin).encode('utf-8'))
        
        # Print Debug
        print(Fore.YELLOW + "[-] {} kicked from the server by {}!".format(nickname, admin))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        
        #Kick
        clients[nickname].shutdown(socket.SHUT_RDWR)
        clients[nickname].close
        del clients[nickname]
    else:
        clients[admin].send("<SERVER> Sorry, but {} already kicked or not exist.".format(nickname).encode('utf-8'))
        
def ban(nickname, admin):
    if nickname not in bans:
        # Send Info
        if nickname in clients:
            clients[nickname].send("[-] You have been banned from the server by {}! Code 403".format(admin).encode('utf-8'))
           
        clients[admin].send("<SERVER> {} successfully banned.".format(nickname).encode('utf-8'))
        broadcast('[-] {} banned on the server by {}!'.format(nickname, admin).encode('utf-8'))
        
        # Print Debug
        print(Fore.YELLOW + "[-] {} banned on the server by {}!".format(nickname, admin))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        
        # Kick
        clients[nickname].shutdown(socket.SHUT_RDWR)
        clients[nickname].close
        del clients[nickname]
        
        # Ban
        bans.append(nickname)
        # Вообще, надо сделать банлист файл, чтобы все сохранялось
        # после рестарта сервака, но пока я ленивая жопа
    else:
        clients[admin].send("<SERVER> Sorry, but {} already banned.".format(nickname).encode('utf-8'))
        
def unban(nickname, admin):
    if nickname in bans:
        # Send Info
        clients[admin].send("<SERVER> {} successfully unbanned.".format(nickname).encode('utf-8'))
        
        # Print Debug
        print(Fore.YELLOW + "[~] {} unbanned on the server by {}!".format(nickname, admin))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        
        # UnBan
        bans.remove(nickname)
        # Вообще, надо сделать банлист файл, чтобы все сохранялось
        # после рестарта сервака, но пока я ленивая жопа
    else:
        clients[admin].send("<SERVER> Sorry, but {} not banned.".format(nickname).encode('utf-8'))       


###############################
##                           ##
##        Server core        ##
##                           ##
###############################
        
# Client Close Function   
def exit(nickname, clients, client):
    if nickname in clients:
        clients[nickname].shutdown(socket.SHUT_RDWR)
        del clients[nickname]
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        broadcast('[-] {} left the server!'.format(nickname).encode('utf-8'))
        print(Fore.YELLOW + "[-] {} left the server!".format(nickname))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)

# Sending Messages To All Connected Clients
def broadcast(message):
    for x in clients:
        clients[x].send(message)
        
# Getting Command Function
def get_commad(message, nickname, clients, client):
    # Get message and nick and cut only message
    message_text = message.decode('utf-8')
    nickcount = len('<' + nickname + '> ')
    message_text = message_text[nickcount:]
    
    # Так, для дебага вывод только сообщения
    print(message_text)
    
    # If message starts from "/"(Command symbol) - get command and execute
    if "/" in message_text:
        #################
        #  Kick module  #
        #################
        if "/kick" in message_text:
            kick(message_text[6:], nickname)                                 # 1 - who kicked    2 - admin name      
        
        #################    
        #   Ban module  #
        #################
        elif "/ban" in message_text:
            ban(message_text[5:], nickname)                                  # 1 - who banned    2 - admin name
        elif "/unban" in message_text:
            unban(message_text[7:], nickname)                                  # 1 - who banned    2 - admin name
        ##################    
        #   Mute module  #
        ##################
        elif "/mute" in message_text:
            mute(message_text[6:], nickname)                                 # 1 - who muted     2 - admin name
        elif "/unmute" in message_text:
            unmute(message_text[8:], nickname)                               # 1 - who unmuted   2 - admin name
            
        #################  
        # System module #
        #################
        elif "/rules" in message_text:
            clients[nickname].send(rules.encode('utf-8'))
        elif "/q" in message_text:
            clients[nickname].send("<SERVER> Exit. Code 1".encode('utf-8'))
            exit(nickname, clients, client)    
        else:
            clients[nickname].send("<SERVER> Unknown command.".encode('utf-8'))  
        return True