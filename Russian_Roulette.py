#=============== sonic_the_cyber_warrior && FURR0404 && N33dT3ch ===============#
#Russian_Roulette.py
import random
import time
#================================#
print("██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗\n██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║\n██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║\n██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║\n██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║\n╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝\n██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗\n██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝\n██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░\n██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░\n██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗\n╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝\n██████╗░██╗░░░██╗  ███╗░░██╗██████╗░██████╗░██████╗░░░░░░██╗███████╗███████╗██╗░░░██╗███████╗\n██╔══██╗╚██╗░██╔╝  ████╗░██║╚════██╗╚════██╗██╔══██╗░░░░░██║██╔════╝██╔════╝██║░░░██║██╔════╝\n██████╦╝░╚████╔╝░  ██╔██╗██║░█████╔╝░█████╔╝██║░░██║░░░░░██║█████╗░░██████╗░██║░░░██║██████╗░\n██╔══██╗░░╚██╔╝░░  ██║╚████║░╚═══██╗░╚═══██╗██║░░██║██╗░░██║██╔══╝░░╚════██╗██║░░░██║╚════██╗\n██████╦╝░░░██║░░░  ██║░╚███║██████╔╝██████╔╝██████╔╝╚█████╔╝███████╗██████╔╝╚██████╔╝██████╔╝\n╚═════╝░░░░╚═╝░░░  ╚═╝░░╚══╝╚═════╝░╚═════╝░╚═════╝░░╚════╝░╚══════╝╚═════╝░░╚═════╝░╚═════╝░")

def roulette():
    print("\n\n\n\n\n\n\n")
    print("______________________\n1) Start\n2) Quit\n______________________\n")
    game = int(input("What is your choice? "))
    
    if game == 2:
        welcomefunct()
    
    if game == 1:
        win=0
        loss=0
        kill_number = (round(random.uniform(1, 6)))
        
        while True:
            for i in range(0, 10):
                chance = random.randint(1, 6)
                if chance == kill_number:
                    for i in range(0, 50):
                        print("\n")
                    loss += 1
                    print("                 ████████████████                ██████")
                    print("            ▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓██            ███")
                    print("          ▓▓░░░░██▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██           █░░░█")
                    print("            ████▓▓██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██           █░░░█")
                    print("            ██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████            ███")
                    print("        ████▓▓▓▓▓▓██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓              ")
                    print("    ██████▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓██                ")
                    print("  ██▓▓▓▓▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                  ")
                    print("    ██▓▓▓▓▓▓▓▓██▓▓██████████████████▓▓                  ")
                    print("    ██▓▓▓▓▓▓▓▓████▓▓  ▒▒    ▓▓                          ")
                    print("  ██▓▓▓▓▓▓▓▓██  ▓▓▓▓  ▒▒    ▓▓                          ")
                    print("  ██▓▓▓▓▓▓▓▓██    ▓▓▓▓▓▓▓▓▓▓                            ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("    ██    ██                                            ")
                    print("      ████                                              ")
                    print("██████╗░░█████╗░███╗░░██╗░██████╗░\n██╔══██╗██╔══██╗████╗░██║██╔════╝░\n██████╦╝███████║██╔██╗██║██║░░██╗░\n██╔══██╗██╔══██║██║╚████║██║░░╚██╗\n██████╦╝██║░░██║██║░╚███║╚██████╔╝\n╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░")
                    
                    print("\n\n _____Statistics_____")
                    print("Win Count: ", win)
                    print("Lose Count: ", loss)
                    print ("Win/Lose Ratio: ", str(win), str("/"), str(loss))
                    kill_number = (round(random.uniform(1, 6)))
                    time.sleep(1.5)
                    


                
                elif chance != kill_number:
                    win += 1
                    for i in range(0, 50):
                        print("\n")
                    print("                  ████████████████                ██████")
                    print("            ▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓██")
                    print("          ▓▓░░░░██▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██")
                    print("            ████▓▓██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██")
                    print("            ██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████")
                    print("        ████▓▓▓▓▓▓██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓              ")
                    print("    ██████▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓██                ")
                    print("  ██▓▓▓▓▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                  ")
                    print("    ██▓▓▓▓▓▓▓▓██▓▓██████████████████▓▓                  ")
                    print("    ██▓▓▓▓▓▓▓▓████▓▓  ▒▒    ▓▓                          ")
                    print("  ██▓▓▓▓▓▓▓▓██  ▓▓▓▓  ▒▒    ▓▓                          ")
                    print("  ██▓▓▓▓▓▓▓▓██    ▓▓▓▓▓▓▓▓▓▓                            ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("██▓▓▓▓▓▓▓▓▓▓██                                          ")
                    print("    ██    ██                                            ")
                    print("      ████                                              ")
                    print(
                        "\n██╗░░░░░██╗░░░██╗░█████╗░██╗░░██╗██╗░░░██╗██╗\n██║░░░░░██║░░░██║██╔══██╗██║░██╔╝╚██╗░██╔╝██║\n██║░░░░░██║░░░██║██║░░╚═╝█████═╝░░╚████╔╝░██║\n██║░░░░░██║░░░██║██║░░██╗██╔═██╗░░░╚██╔╝░░╚═╝\n███████╗╚██████╔╝╚█████╔╝██║░╚██╗░░░██║░░░██╗\n╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝"
                    )
                
                    print("\n\n _____Statistics_____")
                    print("Win Count: ", win)
                    print("Lose Count: ", loss)
                    time.sleep(1.5)


            
            if win == 10:
                print ("\nCongrats!! You survived!!")

            elif loss == 1:
                print ("\nOh no! You died", loss, "time...")
                
            elif loss > 1:
                print ("\nOh no! You died", loss, "times...")

            a = str(input("\n\nPress enter to play again, or x to leave: "))
                
            if a == "x":
                for i in range(0, 5):
                    print(".")
                    time.sleep(0.5)
                exit()

            else:
                win = 0
                loss = 0



                    
#===================================================#
def welcomefunct():
    print("\n\n__Welcome to Russian Roulette__")
    print("1) Play Game")
    print("2) How to play")
    print("3) How this works")
    print("4) Exit\n")
    
    welcome = int(input("What is your choice: "))
    
    if welcome == 1:
        roulette()
        
    elif welcome == 2:
        print(
            "\n\n\nTo play use the numbers provided to navigate the menus. \nPress 1 then enter then 1 then enter to play.\n"
        "Have Fun!\n\n"
        )
        print("1) Back to menu\n2) Credits")
        
        htpmenu = int(input("What is your choice?(int): "))
        
        if htpmenu == 1:
            welcomefunct()
            
        elif htpmenu == 2:
            print("\n\n\n_______________CREDITS_______________")
            print(
                "EMAIL: dmartinez54877@gmail.com\nTwitter: @DanovanMartinez\nGitHub: N33dT3ch\n\n\n"
                "EMAIL: notsonic26@gmail.com\nGithub: s0n1c268\n\n\n"
                "Github: FURRO404\n"
            )
            
            c = input("Press enter to return to menus ")
            welcomefunct()
            
    elif welcome == 3:
        print(
            "\n\nThe game works because it uses 2 functions for the menu and game options"
            )
        print(
            "It uses integers to go through the menus because there are no buttons and it is controlled using the console."
            )
        print(
              "It uses ifs statments and organizing to not be perfect but great.\n\n"
              )
        
        c = input("Press enter to return to menus ")
        welcomefunct()

    elif welcome == 4:
        for i in range(0, 5):
            print(".")
            time.sleep(0.5)
        exit()

    else:
        print("You have negative iq")
        
welcomefunct()
#=============== sonic_the_cyber_warrior && FURR0404 && N33dT3ch ===============#
