import os, sys, time, socket
from colorama import Fore, Back

name = socket.gethostname()
ipv4 = socket.gethostbyname(name)
contador = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def salir():
    os.system('clear')
    print(Fore.RESET + Back.RESET)
    sys.exit()

def error():
    print('\n[>] Error: Command not found :(\n')
    choice = input(f'{name}@BasicWhois: [Presiona cualquier tecla ara volver al menú]: ')
    menu()

def volver_menu():
    choice = input(f'\n{name}@BasicWhois: [Presiona cualquier tecla ara volver al menú]: ')
    menu()

def menu():
    os.system('clear')
    title = f'''
    )                                )              
 ( /(     )     (         (  (    ( /(      (       
 )\()) ( /(  (  )\   (    )\))(   )\())  (  )\  (   
((_)\  )(_)) )\((_)  )\  ((_)()\ ((_)\   )\((_) )\  
| |(_)((_)_ ((_)(_) ((_) _(()((_)| |(_) ((_)(_)((_) 
| '_ \/ _` |(_-<| |/ _|  \ V  V /| ' \ / _ \| |(_-< 
|_.__/\__,_|/__/|_|\__|   \_/\_/ |_||_|\___/|_|/__/

[>] By 3xpl017: https://github.com/3xpl017
[>] Utiliza este software solo con propósitos éticos

[>] Tu IP: {ipv4}
[>] Nombre de tu máquina: {name}
'''
    print(Fore.RED + Back.RESET + title)

    options = '''
[00] Salir
[01] Volver al menú
[02] Hacerle un whois a una IP
[03] Hacerle un whois a un dominio
'''
    print(Fore.BLUE + Back.RESET + options)

    choice = input(f'{name}@BasicWhois:~$ ')

    if choice == '00' :
        salir()

    elif choice == '02':
        print('\n[>] Ingresa la IP:')
        choice = input(f'\n{name}@BasicWhois')
        print('\n[>] Whois {choice}: ')
        print('-----------------------------------------------------------------------------------')
        os.system(f'whois {choice}')
        print('-----------------------------------------------------------------------------------')
        volver_menu()

    elif choice == '03':
        print('\n[>] Ingresa el nombre del dominio:')
        choice = input(f'\n{name}@BasicWhois')
        print('\n[>] Whois {choice}: ')
        print('-----------------------------------------------------------------------------------')
        os.system(f'whois {choice}')
        print('-----------------------------------------------------------------------------------')
        volver_menu()

    else:
        error()

menu()
