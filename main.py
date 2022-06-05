#begin python
import os
import pyautogui
import random
import turtle
from colorama import Fore, Back, Style
import colorama
from time import sleep

os.system('clear')
os.name
import pystyle
from pystyle import Colorate, Colors, Center


header_final = """
 
░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗██████╔╝██║░░██║███████╗███████╗███████╗
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
\n\n\n\n"""

print(Colorate.Diagonal(Colors.cyan_to_green, Center.Center(header_final)))
if os.name == "posix":

    while True:

        cd = input("\n-> ")
        if cd == "help":
            print("\n>>> all commands :\n", "\n - --help (after some commands)", "\n - color","\n - color --back", "\n - myos", "\n - exit", "\n - ping","\n - clear","\n - shutdown", "\n - say","\n - calc")
            #
        if cd == "color":
            print('\n')
            c = input(">>> what color do you want ? -> ")

            if c == "b":
                print(Fore.BLUE, "\n>>> color is blue now !")

            if c == "bl":
                print(Fore.BLACK, "\n>>> color is black now !")

            if c == "r":
                print(Fore.RED, "\n>>> color is red now !")

            if c == "w":
                print(Fore.WHITE, "\n>>> color is white now !")

            if c == "reset":
                print(Fore.RESET, "\n>>> color is reseted now !")
            if c == "g":
                print(Fore.GREEN, "\n>>> color is green now !")
            #
        if cd == "color --help":
            print(Fore.BLUE, "\nb -> BLUE ", Fore.RESET, "\nbl -> BLACK ", Fore.RED, "\nr -> RED", Fore.WHITE,
                  "\nw -> WHITE", Fore.RESET, "\nreset -> RESET", Fore.GREEN, "\ng -> GREEN")
            #
        
        if cd == "color --back --help":
            print("\n", Back.BLUE, "b -> BLUE",Back.RESET,"\n", Back.BLACK, "bl -> BLACK", Back.RESET,"\n",Back.RED, "r -> RED",Back.RESET,"\n", Back.WHITE,Fore.BLACK,"w -> WHITE",Back.RESET,"\n", Back.RESET,Fore.RESET, "reset -> RESET", Back.RESET,"\n", Back.GREEN)
            #

        if cd == "color --back":
            print('\n')
            c = input(">>> what background color do you want ? -> ")

            if c == "b":
                print(Back.BLUE, "\n>>> background is blue now !")

            if c == "bl":
                print(Back.BLACK, "\n>>> background is black now !")

            if c == "r":
                print(Back.RED, "\n>>> background is red now !")

            if c == "w":
                print(Back.WHITE, "\n>>> background is white now !")

            if c == "reset":
                print(Back.RESET, "\n>>> background is reseted now !")
            if c == "g":
                print(Back.GREEN, "\n>>> background is green now !")

        if cd == "exit":
            print("\n",Fore.RED,'>>> you are leaving shell now !')
            
            header_final = """
            \n\n
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
███████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀██████▓▀▀▀▀▀▓█▀▀▀▀▀▓█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█████████
███████████               ╫▓      ▀███╨     ▄█▓     ▐▌                 ▓████████
███████████      ▌▌▌▌▌▌▌▌▌███▌     ╙█      ▓██▓     ▐▓▄▄▄▄▄²     ╓▄▄▄▄▄█████████
███████████      ▀▀▀▀▀▀▀▀▀█████µ         ▄████▓     ▐██████▌     ╫██████████████
███████████              ]██████²       ▀█████▓     ▐██████▌     ╫██████████████
███████████     ]█████████████▀          └████▓     ▐██████▌     ╫██████████████
███████████      ▀▀▀▀▀▀▀▀▀▀██└     ▄▓      ▀██▓     ▐██████▌     ╫██████████████
███████████               ▐▀     ²████▄      ▓▓     ▐██████▌     ╫██████████████
███████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌▄▄▄▄▄▓██████▓▄▄▄▄▄▄█▄▄▄▄▄▓██████▓▄▄▄▄▄▓██████████████
████████████████████████████████████████████████████████████████████████████████
\n\n\n\n"""

            print(Back.RESET,Colorate.Diagonal(Colors.red_to_purple, Center.XCenter(header_final)))
            sleep(0.2)
            quit()
            #

        if cd == "myos":
            print('\n>>> you are on MAC or Linux...(posix)')
        #

        if cd == "clear":
            os.system('clear')
            
            
            print(Fore.RESET, Back.RESET,'Loading...')
            sleep(0.5)
            
            os.system('clear')
            
        #

        if cd == "ping":
            os.system("ping " + input("what ? ->"))
        #

        if cd == "ping -c":
            count = input('how many packages ? -> ')
            what = input("what ? -> ")
            os.system('ping -c '+ count + " " + what)

        #
        if cd == "ping --help":
            print("\n-c -> count of packets")
        #

        if cd == "calc":
            os.system('clear')
            print('\n>>> Welcome on the simpliest calculator ever ! ->\n')
            nbr1 = input('1st number -> ')
            nbr2 = input('2nd number -> ')
            

            os.system('clear')

            
            calc = input('\n>>> what would you i do ? (need help ? write "help") -> ')
            if calc == "help":
                os.system('clear')
                print('\n* -> multiply', "\n+ -> add", "\n- -> subtract", "\n/ -> divide")
            
            if calc == "*":
                s = int(nbr1) * int(nbr2)
                print('{0} * {1} = {2}'.format(nbr1, nbr2, s))

            if calc == "+":
                s = int(nbr1) + int(nbr2)
                print('{0} + {1} = {2}'.format(nbr1, nbr2, s))
            
            if calc == "-":
                s = int(nbr1) - int(nbr2)
                print('{0} - {1} = {2}'.format(nbr1, nbr2, s))

            if calc == "/":
                s = int(nbr1) / int(nbr2)
                print('{0} / {1} = {2}'.format(nbr1, nbr2, s))
            #
        if cd == "mBigerEvent":
            for i in range(100):
                print(Fore.BLUE, Back.RED, "LGBT")
                sleep(0.003)
                print(Fore.GREEN, Back.YELLOW, "LGBT")
                sleep(0.003)
                print(Fore.RED, Back.GREEN, "LGBT")
                sleep(0.003)
                print(Fore.MAGENTA, Back.BLUE, "LGBT")
                sleep(0.003)
                print(Fore.BLACK, Back.MAGENTA, "LGBT")
                sleep(0.003)
            #
        
        if cd == "logo":
            
            l = "e"
            for l in "y" or "n":
                l = input('\n>>> want to see our logo ? (y / n) ->')
                if l == "y":
                    turtle.bgcolor('black')
                    turtle.pensize(2)
                    turtle.speed(11)
                    turtle.hideturtle()
                    for i in range(6):
                        for colours in ["red", "magenta", "blue", 'cyan', "green", "yellow", "white", "brown"]:
                            turtle.color(colours)
                            turtle.circle(100)
                            
                            turtle.left(10)
                    for i in range(6):
                        for colours in ["orange", "cyan", "grey", "green", "yellow", "white"]:
                            turtle.color(colours)
                            turtle.circle(70)
                            
                            turtle.left(100)
                    l = "y"
                    os.system('clear')
                    
                    turtle.exitonclick()
                    
                if l == "n":
                    print("\n>>> ok !")
                    sleep(1)
                    l = "n"
                    os.system('clear')
                #

        if cd =="shutdown -r":
            print('\n>>>restart the computer')
            pyautogui.click(1, 5)
            pyautogui.click(20, 220)

            sleep(0.5)
            pyautogui.click(921,319)
                #

        if cd == "say":
            os.system('clear')
            print(Fore.RED,'\n   >>>write what you want to say(use ^C to leave)->')
            print(Fore.BLUE, Back.RESET)
            os.system('say ')
            #

        if cd == "shutdown -t":
            print('\n>>>total shutdown')
            pyautogui.click(1, 5)
            pyautogui.click(20, 240)

            sleep(0.5)
            pyautogui.click(921,319)
            #

        if cd == "shutdown -s":
            print('\n>>>leaving session')
            pyautogui.click(1, 5)
            pyautogui.click(20, 290)

            sleep(0.5)
            pyautogui.click(921,319)
            #

        if cd == "shutdown --help":
            print('\n-s -> session',"\n-r -> restart", "\n-t -> total")
            #

        
                

