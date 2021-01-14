import os
import sys
import time
import socket
import builtins
import threading
from colorama import init, Fore, Back, Style

# Пригодится... Когда то...
#import sqlite3
#import select
#import errno

#################################
##                             ##
##     Debug initialization    ##
##                             ##
#################################
def debug(clients):
    while True:
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        print("    Clients: " + str(clients))
        print("\33[90m" + """    -----------------------------------"""+ Fore.WHITE)
        
        time.sleep(9)

def init_debug():
    debug_t = threading.Thread(target=debug, args=(clients,))
    debug_t.start()


#################################
##                             ##
##  Variables initialization   ##
##                             ##
#################################
__builtins__["clients"] = {}
__builtins__["bans"]    = []
__builtins__["mutes"]   = []


#################################
##                             ##
##    Server initialization    ##
##                             ##
#################################
def init_server():
    try:
        config = open('main.conf')
        config.readline()
        auto = int(config.readline().rstrip()[6:])
        log = int(config.readline().rstrip()[5:])

        # If AutoInit Enabled - Do
        if auto == 1:
            host = config.readline().rstrip()[4:]
            print("    Auto-init host: " + host)
            port = int(config.readline().rstrip()[6:])
            print("    Auto-init port: " + str(port))
            __builtins__["channel_name"] = config.readline().rstrip()[9:]
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
                
            __builtins__["channel_name"] = "#" + input('    Set channel name: ')
    except:
        print(Fore.YELLOW + "\n    [!]  Сonfig does not exist or has an invalid format!")
        time.sleep(5)
        sys.exit() 

    #Save Init Global Data
    __builtins__["rules"] = config.readline().rstrip()[7:]
    __builtins__["ver"] = 'Alpha 1_5.5.1'

    # На будущее оставлю тут базу
    #conn = sqlite3.connect("base.db")
    #cursor = conn.cursor()

    print("\33[90m" + """
    -----------------------------------""" + Fore.WHITE)

    # Starting Server
    __builtins__["server"] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, port))
        server.listen()
    except:
        print(Fore.YELLOW + "\n    [!]  The given IP or port is busy!")
        time.sleep(5)
        sys.exit() 