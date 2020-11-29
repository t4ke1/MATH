# Imports
import sys
import socket
import select
import errno
import socket
import threading
import time
import os
from termcolor import cprint, colored

cprint("""
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
    """, 'magenta', attrs=['reverse', 'blink'])

time.sleep(2)
os.system('cls||clear')

# Info
cprint("""
     ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ██░ ██ 
    ▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
    ▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
    ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
    ▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
    ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
    ░  ░      ░  ▒   ▒▒ ░   ░     ▒ ░▒░ ░
    ░      ░     ░   ▒    ░       ░  ░░ ░
       ░         ░  ░         ░  ░  ░                                     
    -----------------------------------
    Version: Alpha 1_1
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------

    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!
    -----------------------------------""", 'cyan', attrs=['reverse', 'blink'])

# Client Settings
IP = input('    IP: ')
if IP == '':
    cprint("\n    [!] Please enter IP!", 'yellow')
    time.sleep(5)
    sys.exit()
    
try:
    PORT = int(input('    Port: '))
    if PORT == '':
        cprint("\n    [!] Please enter port!", 'yellow')
        time.sleep(5)
        sys.exit()   
except ValueError:
    cprint("\n    [!] Port must be an integer!", 'yellow')
    time.sleep(5)
    sys.exit()
    
ver = "Alpha 1_1"

# Choosing Nickname
nickname = input('    Username: ')
if nickname == '':
    cprint("\n    [!] Please enter nickname!", 'yellow')
    time.sleep(5)
    sys.exit()

print("""
    -----------------------------------    
""")
# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((IP, PORT))
except socket.error as e:
    if e.errno == errno.ECONNREFUSED:
        cprint("\n    [!] Server refused connection or unavailable", 'yellow')
    else:
        raise

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('utf-8')
            
            #Version Check
            #If Server Sends Conflict Code - Kick
            if "Code 409" in message:
                e1 = colored("░", 'red')
                e2 = colored("░", 'white')
                e3 = colored("░ ", 'red')
                print(e1 + e2 + e3 + message)
                client.close()
                break
            if "Code 401" in message:
                e1 = colored("░", 'red')
                e2 = colored("░", 'white')
                e3 = colored("░ ", 'red')
                print(e1 + e2 + e3 + message)
                client.close()
                break
            else:
                # If 'NICK' Send Nickname
                if message == 'NICK':
                    client.send(nickname.encode('utf-8'))
                    client.send(ver.encode('utf-8'))
                else:
                    e1 = colored("░", 'red')
                    e2 = colored("░", 'white')
                    e3 = colored("░ ", 'red')
                    print(e1 + e2 + e3 + message)
        except:
            e11 = colored(">", 'red')
            e22 = colored(">", 'white')
            e33 = colored("> ", 'red')
            # Close Connection When Error 
            print(e11 + e22 + e33 + "[-] An error occured!")
            client.close()
# Sending Messages To Server
def write():
    while True:
        try:
            message_text = input('')
            # Check for blank massage
            if message_text == '':
                continue
            else:
                message = '<{}> {}'.format(nickname, message_text)
                client.send(message.encode('utf-8'))
        except:
            pass

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

