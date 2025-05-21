import random
import platform
import os
import sys
import re
import time

# Lista que recoge las tres jugadas posibles.
choices = ["piedra", "papel", "tijeras"]

# Por comodidad, y para asegurar la uniformidad visual, utilizaremos siempre esta variable como separador.
separator = "\n****************************************************************************************\n"

# Versión original y más detallada del ascii art.
def fullart():
    print(r"""\
 ____                   __                                ____                          ___                   ______                                          
/\  _`\   __           /\ \                              /\  _`\                       /\_ \                 /\__  _\__    __                                 
\ \ \L\ \/\_\     __   \_\ \  _ __    __                 \ \ \L\ \ __     _____      __\//\ \                \/_/\ \/\_\  /\_\     __   _ __    __      ____  
 \ \ ,__/\/\ \  /'__`\ /'_` \/\`'__\/'__`\                \ \ ,__/'__`\  /\ '__`\  /'__`\\ \ \                  \ \ \/\ \ \/\ \  /'__`\/\`'__\/'__`\   /',__\ 
  \ \ \/  \ \ \/\  __//\ \L\ \ \ \//\ \L\.\_               \ \ \/\ \L\.\_\ \ \L\ \/\  __/ \_\ \_                 \ \ \ \ \ \ \ \/\  __/\ \ \//\ \L\.\_/\__, `\
   \ \_\   \ \_\ \____\ \___,_\ \_\\ \__/.\_\               \ \_\ \__/.\_\\ \ ,__/\ \____\/\____\                 \ \_\ \_\_\ \ \ \____\\ \_\\ \__/.\_\/\____/
    \/_/    \/_/\/____/\/__,_ /\/_/ \/__/\/_/                \/_/\/__/\/_/ \ \ \/  \/____/\/____/                  \/_/\/_/\ \_\ \/____/ \/_/ \/__/\/_/\/___/ 
                                                                            \ \_\                                         \ \____/                            
                                                                             \/_/                                          \/___/                             


                                                                                       -*++*   ::.:...:::=-=--.:%@
                                                                                      %*=-:* +    .:::::=++-=:.=+@
                                                                                     =   .:::@@*   .::-::-=-:-==%=
                                                                                   +***%= :=:=. %@  :.:-:=++:=-:@
                                                                                  ==:::.=%%:      :  ::::=**=:-.=
                                                                                 *-:--*+*:.=%@%.     : :::=-=..%@@@=
                                                                               %%*+:::. :+%%*%%@@@@@ :   :=-: *@%=-%=
                                                                             %#==**%*-====::::.:%@@@ .  :-. : :@=::@=
                                                                           *%+=+=-:==*-. :  :@@@@**@  :::==%%-.#:%%
                                                                         +%+.:::--=-:*+=*+%@@+:   :@@  =-.: :*:#:%
                                                                       +#*=*%.::-==*##=   :     *@+%=  # -=++*:+%*
                                                                     .+=::-:+:-:+%%: -*%@%*-=-=@     :  : :.. =%+
                                    =*=   @%*+=:                    *==::-===*%%@   *-::-=*%%#@= .:  ==*     @%*
                                   @%*: *@%*==:-                 -%%* .::-+#%%.     *::. :==+*@@-  .:::=**#@@@
                                  @%=:  %%*%==..==:            :#=.:=*::=%%%        +.   .=-*-  @@%%%%@@===
                                 @%%+=  @==*:: %*:==.        :%=:::-=*%@%           =:=*--:-%
                           @%%%@@*+*=  @%-==:  @* :*=       ***++*+#%@              =::=+%=%%
                         -@#-  @=**+  @=.=#*: @#*:-=        -.:.:%%@                :::-===%
                        @%%=: .@ .   @@---   *%..-:=         +#%%-                 .:.::===%                                ::
                       @#==+  @=:-:  @::==: .@*==-:=                               .: ::=**-                             -==-::-+
                     .@+*%*. @@=++. @*+**=  @: : .::                               ::==::+%                             -: :::::=*+
                    =%*-:   @.:%%-:@::#%= %@-:::.--                                =::=+*%#                .===**%**+=*#+#+=.:-=#*%**
                   #@%%%#= @= .   @ :.   +@ :-=-::-                               :--::=*%                =:.              =:-=-+=-:=*+
                  @*=::.  *%--=  =%.-.   @-:+=+=-+.                               ::.-+##-               +:-===:: :=   .:#:   =+@==+=*+#
                 @*--::   @@@%**@@:--: :@. ::--++#                                *+=-=#%                #=-:=:::  @*-=+: =*+**#=-*+==-=%
               %@@#%%%%%@@      =#=@#=%@: =::.  :                                ::::=*%                 .%**=:.:. :@@@::.. ++     ::.=*@%
              @%*-::       =- .    .-.@@  =::::-+                                 -+*%%+                  :#%%@@@@@=  ::+%%+=@@@@@@@@@%%===
             @%+=:=-:-: . :%--. =:  *: %@*-:.:-*                                                        #==%%+:  :+@@@@@@@@@@%-.--. . .-=#*#
            @@::-:==-==::.%**--+*=:+*=   :@@%*%                                                         +=.             .=**#@@   :-:==:-+=%
           +@=**%++=:. . :*:: :==+#*=::      =.                                                         =%: ...:--=-:         %@*+==-::====#@
           @=::  :=%%%@+%%%+%%*=-+=+#=++=::.-*        :*-                                               :-@==.:-=*+*--=-==--. @@%+==-:=*==-*#%
          ##==:::           ::.:-== ..-==:..=.    *@%**=-=+                                            =-  =@@@*         .:  :@#%**+==-::=***%%*.
          @=---:-:=:-==*##=: .====*%@@%#*%*%=   @@%%====-=#=                                           :=      %@@@@@@@@@@@@@#%+===-====+*+**#*++=*=
          %=-::::-=-:.. ..  -: .-          *  @@%+-:-=*%%                                              .*: :            :-::@:#%===========+*====::=+*=
         @*--:.::.:-:::=: :+:#+=--::     @@@%%*@%+::=+*                                                 @=:-:=+**=-+-::::.  @=-+*%+=====+=++-=*=++=====#*:
         @====--::::.:=. *-*:-:---:-:  :@@ = .  =%=:=*                                                  +@*:--=+**=:     :+@@#==:=+==---==+=**+======--:=*#
         %=:-:::::::-:-=*===:====++-:  :%  :.:--  #%%                                                   =-:@@@=  :#@@@@@@@:::%:=+*=+=+*+===+**===+==--=:-=-
        @+=-=-::.:=--:*=:-::=:::=-:.:=*  :.:.-:=+%%                                                      @- .+@@@%          @@-:=-+*=:=*=*=*=++*-==+=-===--
       @*=-==-::==-:-=-:-==::--::.:::.: .=:-::+%+                                                         @*:. .:::==++**+:%@=-:--:==::*=**:+=*++==+==-==-=
     =@%--===-::--==-=:--::-:---:::-:--:-: :+%=                                                            @@%+=-=*-::::..@@=:---====:-=*-=:=+-:=*====-====
    @@==-=======--==-=-:-:::-.:::::.:=:=*#%@:                                                                @@%*::=@%*%%*%=.:-=--===:+=++-+++=+**=========
   @%==-==-=*======-===:==--::::.:-:-=+@@#                                                                      *@@@@@@@@@@@@@@%=-::=*%=:+*===+====-=======
  @*====:-==-+====:-=-::-:--+=-:::+*@@.                                                                                        *@@@%=-=+*===++=----====--==
 @*-===-*==---:=+===-***++=-=:+%@@@                                                                                               -@@@*=====-:---==-=--====
 +---=+===**+=*=+*##***%%@@@@@@+                                                                                                     %@@%*----=====-=-==-::

        """)

# Versión más comprimida del ascii art.
def miniart():
    print(r"""\
            ____                   __                                         
           /\  _`\   __           /\ \                                        
           \ \ \L\ \/\_\     __   \_\ \  _ __    __                           
            \ \ ,__/\/\ \  /'__`\ /'_` \/\`'__\/'__`\                         
             \ \ \/  \ \ \/\  __//\ \L\ \ \ \//\ \L\.\_                       
              \ \_\   \ \_\ \____\ \___,_\ \_\\ \__/.\_\                      
               \/_/    \/_/\/____/\/__,_ /\/_/ \/__/\/_/                      
                     ____                          ___                        
                    /\  _`\                       /\_ \                       
                    \ \ \L\ \ __     _____      __\//\ \                      
                     \ \ ,__/'__`\  /\ '__`\  /'__`\\ \ \                     
                      \ \ \/\ \L\.\_\ \ \L\ \/\  __/ \_\ \_                   
                       \ \_\ \__/.\_\\ \ ,__/\ \____\/\____\                  
                        \/_/\/__/\/_/ \ \ \/  \/____/\/____/                  
                                       \ \_\                                  
                              ______    \/_/                                  
                             /\__  _\__    __                                 
                             \/_/\ \/\_\  /\_\     __   _ __    __      ____  
                                \ \ \/\ \ \/\ \  /'__`\/\`'__\/'__`\   /',__\ 
                                 \ \ \ \ \ \ \ \/\  __/\ \ \//\ \L\.\_/\__, `\
                                  \ \_\ \_\_\ \ \ \____\\ \_\\ \__/.\_\/\____/
                                   \/_/\/_/\ \_\ \/____/ \/_/ \/__/\/_/\/___/ 
                                          \ \____/                            
                                           \/___/                             

                                                #+=*=   ::+#-.@=                       
                                              :@@-   :%  :=%=-@                        
                                             -+==#@@@    .:#=:@@                       
                                           *@@@=:*==%@@@   :.:@@@                      
                                         :@#*=+%=:.@@@%@ :*#@:@%                       
                                       :%@@:+@@%@=   = * - -+*@                        
                    %. @@*            *=:%@@@  ==*@@@#   +  @@                         
                   @@ @@@-.:        %+@%@@     =  :% @@@@@@@                           
               %@=@@= @%= @*%-    @@@@@@       =*@@@                                   
              @% @+- @=  @@=%    :@@@          :-*@                                    
            +@@:@@- @%-  @=:+                  :-*@                 *=:*               
           %@#  @=:@%==@@= -                  -=%@@         :-%=+:=-#-+@@%             
          @@* =@+  %   @-#%%                  *-@@         +*-  :  .  =@*%@*           
         @@@@@@: @@@*@@   =+                 =%@@=         @#   %@+.:+* .+#@@          
       %@%.    *    -@@+:-+                               :%@@@@@@@@@@@@@#**@+         
       @%**+= %@:*%%+  =@@                                #         *%@  .-=#@:        
      @+. =**=@%@++*%*=       %*                          -@@#**=     @@%=-+=@@        
     :@=-::  =*  =%@@%*#%  @@@@@@                         -   @@@@@@#@@%==+=#@@@%+     
     @#:::=:.: ===     @ @@@=%@                           @-         @+@#===*#*##%%%@  
     @*=-: :=+%*++**  @*=  @@%                            @@@*#%%@@@@@=-*#*+**%*+*+=+% 
    @%*-.:==*+=--=-::   .=%@                               @*@@+.:   @-:=#:%***%**#+== 
   @@=+-:=*+-:::=-:-=-+*@*                                  @@%%%%%%@@.-==:**=+=*#***+ 
 -@%=+*#*+===:-::.:*@@@:                                      :@@@@@@@@@@*%%*#*#**=*** 
 @#+*+==+*=+%#%@@@@@                                                    +@@@*+=-:=====

        """) 

# Función que fuerza al programa a finalizar sin mostrar el mensaje de error que mostraría al pulsar Ctrl + C.
def exit():
    while True:
        try:
            sys.exit(0)
        except KeyboardInterrupt:
            exit()

# Función que limpia la pantalla y vuelve a lanzar el programa desde el principio.
def reset():
    os.system("clear||cls")
    main()

# Función que maneja la elección del jugador.
def choice_loop():
    global player_choice
# Solicita entrada de texto al jugador para que haga su elección, no distingue entre mayúsculas y minúsculas.
    player_choice = input("¿Piedra, papel o tijeras?: ").strip().lower()

# Si el jugador introduce "salir", finaliza el programa. Si introduce "reset", limpia la pantalla y vuelve a lanzarlo desde el principio.
    if player_choice == "salir":
        raise KeyboardInterrupt
    if player_choice == "reset":
        reset()

# Si el jugador introduce un valor no válido, solicita entrada de texto de nuevo.
# Repite el loop hasta que se introduce un valor válido (piedra, papel o tijeras).
    else:
        while player_choice not in choices:
            print("\nCreo que no te he entendido bien... Probemos de nuevo.\n")
            choice_loop()

# La función game_round() ejecuta una ronda completa.
def game_round():
    global computer_score, player_score, player_name
# La elección de la CPU es aleatoria.
    computer_choice = random.choice(choices)    
    choice_loop()

# Una vez hecha la elección, se juega la ronda. 
    print(separator)
    time.sleep(0.85)
    print("Piedra, papel o tijeras...")
    time.sleep(0.85)
    print("\nA la de una...")
    time.sleep(0.85)
    print("\nA la de dos...")
    time.sleep(0.85)
    print("\n¡Y a la de tres!\n")
    time.sleep(0.85)

    if computer_choice == "piedra":
        print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    elif computer_choice == "papel":
        print("""
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """)

    elif computer_choice == "tijeras":
        print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

# Dependiendo de las elecciones del jugador y de la CPU, se añade un punto al marcador correspondiente.

    if player_choice == "piedra":
        print("""
                        _______
                       (___    '---
                      (_____)
                      (_____)
                       (____)
                        (___)__.---

    """)
        if computer_choice == "papel":
            time.sleep(0.85)
            print("Papel envuelve a piedra. ¡Has perdido!")
            computer_score += 1 
        elif computer_choice == "tijeras":
            time.sleep(0.85)
            print("Piedra aplasta a tijeras. ¡Has ganado!")
            player_score += 1

    elif player_choice == "papel":
        print("""
                        _______
                   ____(____   '---
                  (______
                 (_______
                  (_______
                    (__________.---

    """)
        if computer_choice == "tijeras":
            time.sleep(0.85)
            print("Tijeras cortan a papel. ¡Has perdido!")
            computer_score += 1
        elif computer_choice == "piedra":
            time.sleep(0.85)
            print("Papel envuelve a piedra. ¡Has ganado!")
            player_score += 1

    elif player_choice == "tijeras":
        print("""
                        _______
                   ____(____   '---
                  (______
                 (__________
                      (____)
                        (___)__.---

    """)
        if computer_choice == "piedra":
            time.sleep(0.85)
            print("Piedra aplasta a tijeras. ¡Has perdido!")
            computer_score += 1
        elif computer_choice == "papel":
            time.sleep(0.85)
            print("Tijeras cortan a papel. ¡Has ganado!")
            player_score += 1

# En caso de empate, no se añade ningún punto.
    if player_choice == computer_choice:
        time.sleep(0.85)
        print("¡Empate!")

# Al terminar una ronda, se muestra el marcador.
    print(separator)
    print(f"[{player_name.upper()}]    {player_score} - {computer_score}    [CPU]")
    print(separator)

# Función principal que almacena el resto del programa.
def main():
    global computer_score, player_score, player_name
    try:
# Determina el tamaño de la ventana y extrae dos valores numéricos del string resultante de os.get_terminal_size; uno para las columnas y otro para las líneas.
        size = os.get_terminal_size()
        str_size = str(size)
        numbers = re.findall(r'\d+', str_size) 
        columns, lines = map(int, numbers)

# Si la ventana es demasiado pequeña, la aumenta de tamaño para poder mostrar la versión más detallada ascii art, si el sistema operativo es Windows.
# En otros sistemas operativos que no permiten cambiar el tamaño del emulador de terminal mediante comandos, muestra la versión comprimida del ascii art.
        if columns < 160 or lines < 62:
            if str(platform.system()) == "Windows":
                os.system("mode con cols=160 lines=62")
                time.sleep(0.2)
                fullart()
            else:
                miniart()

# Si la ventana tiene el tamaño apropiado, muestra la versión más detallada del ascii art.
        else:
            fullart()

        print(separator)

# Longitud mínima y máxima del nombre del jugador.
        min_length = 1
        max_length = 12

# Introducción del nombre del jugador.
        while True:
            player_name = input("Introduce tu nombre: ").strip()
            if len(player_name) < min_length:
                print("\nPor favor, introduce al menos un caracter. El campo de nombre no puede quedar vacío.\n")
            elif len(player_name) <= max_length:
                break
            else:
                print(f"\n¡Demasiado largo! Por favor, introduce como máximo {max_length} caracteres.\n")

        print(f"\nBienvenido, {player_name}.", end=" ")

# Lista de posibles modos de juego.
        gamemodes = ["3", "5", "0"]

# Selección del modo de juego.
        while True:
            game_mode = input("¿Cómo quieres jugar?\n\nAl mejor de [3]      Al mejor de [5]      Modo infinito [0]      [salir] [reset]\n\n").strip().lower()
            if game_mode == "salir":
                raise KeyboardInterrupt
            if game_mode == "reset":
                reset()
            else:
                if game_mode in gamemodes:
                    break
            print("\nValor no válido. Por favor, introduce 3, 5 o 0.\n")
            
        print(f"\nBien, {player_name}, comencemos...")
        print(separator)
        time.sleep(0.85)
        print("En cualquier momento, presiona [Ctrl] + [C] o escribe [salir] para salir del programa. También puedes escribir [reset] para volver a empezar.")
        print(separator)

# Marcador que lleva la cuenta de las rondas ganadas por el jugador y por la CPU.
# Se encuentra dentro de main() para que los valores se mantengan entre rondas, pero vuelvan a 0 al resetear.
        player_score = 0 
        computer_score = 0

# Este loop llama a la función game_round, repitiendo el juego hasta que salga un ganador.
# La puntuación necesaria para detener el loop dependerá del modo de juego seleccionado.
# En el modo infinito, el loop nunca se detiene.
        while True:
            if game_mode == "3":
                if player_score == 2:
                    print("¡Felicidades, has ganado la partida!")
                    break
                if computer_score == 2:
                    print("Vaya... has perdido la partida...")
                    break
            if game_mode == "5":
                if player_score == 3:
                    print("¡Felicidades, has ganado la partida!")
                    break
                if computer_score == 3:
                    print("Vaya... has perdido la partida...")
                    break
            game_round()

# Al terminar la partida, ofrece la opción de salir o volver a empezar desde el principio.
        end_of_game = input("\n[salir]      [reset]\n\n").strip().lower()
        if end_of_game == "salir":
            raise KeyboardInterrupt
        if end_of_game == "reset":
            reset()

# Excepción para evitar mensaje de error al pulsar Ctrl + C.
    except KeyboardInterrupt:
        while True:
            try:
                input("\nPresiona [Intro] para salir...")
                sys.exit(0)
            except KeyboardInterrupt:
                exit()

reset()