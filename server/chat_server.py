import socket
import select
import errno
from colorama import init, Fore, Back, Style
import socket
import threading
import os
import time
import sys
import sqlite3

from res.init import * 
from res.core import *


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
    Version: Alpha 1_5.5.1
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

#Start Listening
init_server()
init_debug()
receive()



