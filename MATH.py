import os
import sys
import math
import time

def about():
    print("""
    ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ██╔████╔██║███████║   ██║   ███████║
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
    
    -----------------------------------
    Author: Wiskey666
    Mail: 1488step@horsefucker.org
    DS: yourmomgay#1488
    -----------------------------------

    This is shit that works with network, http and other things. ok. jk ok

    -----------------------------------
    """)   
        
#Main code
about()

aboute = {'Author': 'Wiskey666',
          'Mail': '1488step@horsefucker.org',
          'DS': 'ypurmomgay#1488'
          }
print(aboute)

author = input('A> ')
mail = input('M> ')
dsn = input('DS name> ')
dst = input('DS tag> ')

aboute['Author'] = author
if '@' in mail:
    aboute['Mail'] = mail
else:
    print('Wrong mail.')
aboute['DS'] = dsn + '#' + dst

print(aboute)


