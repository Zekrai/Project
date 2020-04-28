
# Imports
import sys
import time


class Player:
    def __init__(self, name, job, level, xp, next_level, hp, mp, atk, defense, spatk, spdef, dodge,
                 status_effects, game_over):

        self.name = name
        self.job = job
        self.level = level
        self.xp = xp
        self.next_level = next_level
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef
        self.dodge = dodge
        self.status_effects = status_effects
        self.game_over = game_over


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Title Screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == "1":  # PLAY
        start_game()
    elif option.lower() == "2":  # HELP
        help_menu()
    elif option.lower() == "X":  # EXIT
        sys.exit()
    elif option.lower() not in ["1", "2", "X"]:
        print("Please enter a valid command.")
        if option.lower() == "1":
            start_game()
        elif option.lower() == "2":
            help_menu()
        elif option.lower() == "X":
            sys.exit()


def title_screen():
    print("#######################")
    print("#  My RPG adventure!  #")
    print("#######################")
    print("#      - Play - (1)   #")
    print("#      - Help - (2)   #")
    print("#      - Exit - (X)   #")
    print("#######################")
    title_screen_selections()


def help_menu():
    setup_game()
    print("#######################")
    print("#    How to play!     #")
    print("#######################")
    print("#                     #")
    print("#                     #")
    print("#      - Exit - (X)   #")
    print("#######################")
    title_screen_selections()


def start_game():
    setup_game()
    print("#######################")
    print("#     Game start!     #")
    print("#######################")
    print("#                     #")
    print("#     Please wait     #")
    print("#                     #")
    print("#######################")

    time.sleep(3)
    setup_game()
    intro_choice()

# interactions !!! finish actions loop !!! Change actions into fast orders


def prompt():
    print("\n ========================")
    print(" What would you like to do?")
    action = input("> ")
    acceptable_action = ["explore", "inventory", "spells", "abilities", "rest", "quit"]
    while action not in acceptable_action:
        print("Unknown action, try again.\n")
        action = input("> ")
        if action == "rest":
            exit()
        elif action == "return":
            exit()
        elif action == "explore":
            exit()


# setup game !!! issue on system clean !!! temporary fix spamming new lines
def setup_game():
    #   os.system(cls)
    print("\n"*80)


# player intro choices
def intro_choice():
    delay_print("Welcome in text RPG world, I'm the one in charge of this dimension.\n"
                "Why are you here you ask? Well, I'm not sure of the details but you seem to have died on your world.\n" 
                "Oh ... Yeah, indeed you died. See the bright side : you're given a new life here.\n" 
                "Ahem! Anyway, I need to not lose track. I still need to do my mission.\n" 
                "I'll be your guide before allowing you to venture out.\n" 
                "You can call me as you'd like to make our conversations easier, but please tell me your name.\n")

    # name choice
    print('please insert your name.\n')
    name = input('> ')
    delay_print('So your name is ' + name + ", that's quite nice I like it.\n")
    
    # class choice
    delay_print("Please select the class you wish to incarnate.\n")
    job_question = input("Warrior: 1 | Mage: 2 | Thief: 3 | Paladin: 4\n")
    while job_question in ["1", "2", "3", "4"]:
        if job_question == "1":
            job = 'Warrior'
            print("Choice confirmed! You are now a " + job + "!\n")
        elif job_question == "2":
            job = "Mage"
            print("Choice confirmed! You are now a " + job + "!\n")
        elif job_question == "3":
            job = "Thief"
            print("Choice confirmed! You are now a " + job + "!\n")
        elif job_question == "4":
            job = "Paladin"
            print("Choice confirmed! You are now a " + job + "!\n")
        break
    time.sleep(5)
#    os.system(cls)
    print("\n"*80)
    print("##############################")
    print("# Sending you into the abyss #")
    print("##############################")
    time.sleep(3)
    print("\n" * 80)


title_screen()
