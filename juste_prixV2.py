#libraries import

import os
import time
from pystyle import Colors, Colorate, Add
from random import randint
def Replay():
    replay = input("Souhaitez vous rejouer ? ( oui / non ) : ")
    if replay == "non":
        banner0 = '''
     ████████████████████████████████                
  ██                                ██              
██                                  ░░██            
██    ██████    ██    ██  ████████    ██            
██    ██    ██  ██    ██  ██          ██            
██    ██████░░    ██████  ██████      ██            
██    ██    ██        ██  ██          ██            
██    ██████      ████    ████████    ██            
██                                    ██            
  ██                                ██░░            
    ████████      ██████████████████                
    ░░░░░░  ██    ██  ░░░░░░░░░░░░                  
              ██  ██                                
              ██  ██                                
                ████                                
            ██    ██      ██                        
          ██░░██        ██░░██                      
          ██░░▓▓████████▓▓░░██               ████  
        ██░░░░░░▒▒▓▓░░▓▓░░░░▒▒██            ██░░░░██
        ██░░░░░░░░░░░░░░░░░░░░██            ██░░░░██
      ██░░░░██░░░░██░░░░██░░░░▓▓████████      ██▒▒██
      ██░░░░░░░░██░░██░░░░░░░░░░▓▓░░▓▓░░██    ██░░██
      ██░░░░░░░░▒▒░░░░░░░░░░░░░░▓▓░░▓▓░░▒▒██████▓▓██
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
      ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
      ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
      ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██    
        ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██      
          ██▓▓░░░░░░░░▓▓░░░░░░▓▓░░▓▓▓▓░░▓▓██        
            ██░░████░░██████████░░████░░██          
            ████    ████      ████    ████        '''
        text = ""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Add.Add(banner0, text, True))
        time.sleep(2)
        exit()
    elif replay == "oui":
        os.system('cls' if os.name == 'nt' else 'clear')
        boucle_du_jeu()
    else:
        print("Veuillez saisir oui ou non.")
        Replay()

def boucle_du_jeu():                #the main loop
    jeu = 0
    banner1 = '''
88,dPYba,,adPYba,   ,adPPYba,  8b,dPPYba,   ,adPPYba, 8b       d8  
88P'   "88"    "8a a8"     "8a 88P'   `"8a a8P_____88 `8b     d8'  
88      88      88 8b       d8 88       88 8PP"""""""  `8b   d8'   
88      88      88 "8a,   ,a8" 88       88 "8b,   ,aa   `8b,d8'    
88      88      88  `"YbbdP"'  88       88  `"Ybbd8"'     Y88'     
                                                          d8'      
                                                         d8'  '''
    text = ""
    print(Add.Add(banner1, text, True))
    print("Voici les niveaux et leur intervalle respectifs : ")
    print()

#say the level

    print(Colorate.Color(Colors.green, "1 = [0€;10€]", True))
    print(Colorate.Color(Colors.yellow, "2 = [0€;30€]", True))
    print(Colorate.Color(Colors.orange, "3 = [0€;60€]", True))
    print(Colorate.Color(Colors.red, "4 = [0€;100€] ( DOOM SLAYER mode )", True))
    print()
    niveau = int(input("Définissez le niveau dans lequel vous voulez jouer : "))
    print()
    print()

#the level choice

    print("Vous avez choisis le niveau {}.".format(niveau))

#the interval in function of the level

    if niveau == 1:
        nombre_cache = randint(0, 10)
        intervalle = "0€ et 10€"
    if niveau == 2:
        nombre_cache = randint(0, 30)
        intervalle = "0€ et 30€"
    if niveau == 3:
        nombre_cache = randint(0, 60)
        intervalle = "0€ et 60€"
    if niveau == 4:
        nombre_cache = randint(0, 100)
        intervalle = "0€ et 100€"

#the challenge

    while jeu == 0:
        text = "La somme est entre "+intervalle
        print(Colorate.Color(Colors.gray, text, True))
        nombre_devine = int(input("Entrer une somme : "))
        #the indications
        if nombre_devine < nombre_cache:
            text = "Plus cher"
            print(Colorate.Color(Colors.dark_green, text, True))
        elif nombre_devine > nombre_cache:
            text = "Moins cher"
            print(Colorate.Color(Colors.dark_red, text, True))
        else:
            jeu = 1
            banner2 = '''
░██████╗░░██████╗░
██╔════╝░██╔════╝░
██║░░██╗░██║░░██╗░
██║░░╚██╗██║░░╚██╗
╚██████╔╝╚██████╔╝
░╚═════╝░░╚═════╝░    '''
            text = ""
            print(Add.Add(banner2, text, True))
            print("Bravo vous avez gagné ! La somme était bien {}".format(nombre_cache))
            Replay()    #make a call to the Replay function

boucle_du_jeu()

