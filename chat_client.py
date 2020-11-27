import sys
import socket
import select
import errno
from colorama import init, Fore, Back, Style
import socket
import threading
import time

from win10toast import ToastNotifier

toaster = ToastNotifier()

init(convert=True)

print("\033[36m" + """
    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ██╔████╔██║███████║   ██║   ███████║
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

    -----------------------------------
    Version: Alpha 1_0.5
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------

    This is a console chat for special lovers of this shit.
    The chat will be improved (both the client side and the server side).
    Thank you for noticing and trying it!

    -----------------------------------
        IP     Port        Name
    aoa.pp.ua  55555  #general_server
    -----------------------------------
""")
print(Style.RESET_ALL)

IP = input('    IP: ')
PORT = int(input('    Port: '))

# Choosing Nickname
nickname = input('    Username: ')

print("""
    -----------------------------------    
""")
# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(Fore.GREEN +'░' + Fore.YELLOW + '░' + Fore.GREEN + '░ ' + Fore.WHITE + message)
                #print(Style.RESET_ALL)
        except:
            # Close Connection When Error 
            print(Fore.GREEN +'>' + Fore.YELLOW + '>' + Fore.GREEN + '> ' + Fore.RED + "[-] An error occured!")
            client.close()
            break
        
# Sending Messages To Server
def write():
    while True:
        try:
            message = '<{}> {}'.format(nickname, input(''))
            client.send(message.encode('ascii'))
        except:
            pass

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

