import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Global variables
player_health = 75
player_attack = 10
player_defense = 6
player_inventory = ["A healing potion"]

# Introduction and initial setup
def start_game():
    print("Welcome to the this adventure game!")
    print("You are about to embark on an epic journey filled with challenges and mysterious obstacles.")
    print("Your goal is to complete each task so that you can reach your village on the other side of the woods.")
    print("Are you ready for the adventure of a lifetime?")
    player_name = input("What is your name? ")
    clearConsole()
    print(f"Welcome {player_name} to the Damned Willow Forest!")
    print("You find yourself standing at the dense growing trees, wondering how you will get by.")
    print("As you look ahead, you notice a signpost that lists several tasks that must be completed")
    print("before you can continue on your journey.")
    print("The tasks you must complete will test your skills and determination so you can get home.")
    print("Are you ready? Take a deep breath, and let the adventure begin!")
    choice = input("Are you ready to continue? Type 'y' for yes or 'n' for no: ")
    if choice == 'y':
        clearConsole()
        print(f"Here is some valid information about your character: \n Health: {player_health}\n Attack: {player_attack}\n Defense: {player_defense}\n Inventory: {player_inventory}\n")
        input("Press any key to enter the woods: ")
        clearConsole()
        path_choice()
    elif choice == 'n':
        print("Thanks for playing! Have a good day!")
        game_over()
    else:
        print("Invalid choice, please type 'y' for yes or 'n' for no")
    start_game()
    return
        
# First path choice the player encounter
def path_choice():
    print("Lets get started. Do you want to move forward? Type 'y' for yes and 'n' for no and quit game")
    choice = input("> ")
    if choice == 'y':
        clearConsole()
        riddle_encounter()
    elif choice == 'n':
        game_over()
    else:
        print("Invalid choice, please type 'y' or 'n'")
        path_choice()

# Solve the riddle, gives different options for the player to choose from
def riddle_encounter():
    riddles = ["What starts with an E, ends with an E, but only contains one letter?"]
    riddle = random.choice(riddles)
    print("You come across a treasure chest and a sign with a riddle written on it, to open the chest you must answer correctly! ")
    print(riddle)
    print("1. Elephant")
    print("2. Envelope")
    print("3. Eagle")
    print("4. Edge")
    answer = input("What is your answer? ")
    if answer.lower() == "2":
        clearConsole()
        print("Correct! The chest is open! You collect the treasure inside! You may continue on your journey.")
        print("And you continue to move further into the woods")
        clearConsole()
        path_choice_2()
    else:
        print("Incorrect. You have failed the task.")
        game_over()

# Fight the enemy
def player_encounter_goblin():
    goblin_health = 40
    goblin_attack = 15
    global player_inventory 
    player_inventory = []

    print("You have come across a nasty forest goblin!")
    print("Do you want to attack or run away?")
    print("Enter 'a' to attack or 'r' to run away!")
    choice = input("> ")
    while goblin_health > 0:
        if choice == 'a':
            global player_health
            player_attack = random.randint(10, 14)
            goblin_health -= player_attack
            if goblin_health <= 0:
                clearConsole()
                print("You have defeated the goblin! You may continue on your journey.")
                player_inventory.append("Badge of Honor")
                print(f"You have recieved a 'Badge of Honor', it has been added to your inventory")
                print("Well done, where do you want to go now?")
                print("Enter 'r' to go right or enter 'f' to go forward!")
            choice = input("> ")
            if choice == 'r':
                path_choice_4()
            elif choice == 'f':
                if "Book of Wisdom" in player_inventory and "Badge of Honor" in player_inventory:
                    meet_wizard()
                else:
                    print("You are not ready to go there yet, try another way.")
                    choice = input("Enter 'r' to go to the right")
                    if choice == 'r':
                        path_choice_4()
                    else:
                         print("Invalid choice, please type 'r' or 'f'")
                    return
            else:
                print(f"The goblin now has {goblin_health} health.")
                player_health -= goblin_attack
                if player_health <= 0:
                    clearConsole()
                    player_death()
                else:
                    print(f"You now have {player_health} health.")
                    choice = input("Do you want to attack or run? ")
        elif choice == 'r':
            run_away_chance = random.randint(10,14)
            if run_away_chance <= 30:
                print("You managed to run away safely.")
                player_inventory.append("Badge of Honor")
                print(f"You have received a 'Badge of Honor' for at least trying! It has been added to your inventory.")
                clearConsole()
                print("Enter 'r' to go right or enter 'f' to go forward!")
            choice = input("> ")
            if choice == 'r':
                path_choice_3()
            elif choice == 'f':
                if "Book of Wisdom" in player_inventory and "Badge of Honor" in player_inventory:
                    meet_wizard()
                else:
                    print("You are not ready to go there yet, try another way.")
                    choice = input("Enter 'r' to go to the right")
                    if choice == 'r':
                        path_choice_3()
                    else:
                         print("Invalid choice, please type 'r' or 'f'")
                return
            else:
                print("You failed to run away and the goblin hit you.")
                player_health -= goblin_attack
                if player_health <= 0:
                    clearConsole()
                    player_death()
                else:
                    print(f"You now have {player_health} health.")
                    choice = input("Do you want to attack or run? ")
        else:
            print("Invalid choice, please type 'a' or 'r'")
            choice = input("> ")

# Path choice nr 2, here the player has to make choice if to go to path choice 3 or path choice 4
def path_choice_2():
    print("The air is damp and filled with the scent of old trees")
    print("The soft rustling of leaves scared you a bit, anything could be hiding in the bushes")
    print("You get further in to the forest, there are huge tree logs laying everywhere.")
    print("There is one big one in the middle of the road, you have to climb over it to keep going")
    print("Type 'y' for yes to climb the log or type 'g' to go another way.")
    choice = input("> ")
    if choice == 'y':
        clearConsole()
        path_choice_3()
    elif choice == 'g':
        clearConsole()
        path_choice_4()
    else:
        print("Invalid choice, please type 'y' or 'n'")
        path_choice_2()
    return

# path choice nr 3 whhich leads up to the goblin/enemy encounter
def path_choice_3():
    print("You can barely see anything now, the light that once shined through the tree tops is now a distant memory")
    print("This is the last time I leave my house, you mutter. It's just not worth it")
    print("You keep on walking, jumping over the big branches streching over the pathway")
    print("You sense that you are not alone, someone is watching you. But where?")
    print("You stop in your tracks, the smell of something rotten hits you!")
    print("Do you want to keep going? Type 'y' for yes or 'n' for no and run away.")
    choice = input("> ")
    if choice == 'y':
        clearConsole()
        player_encounter_goblin()
    else:
        clearConsole()
        print("You have no choice")
        player_encounter_goblin()
        return

# Path choice nr 4 which leads up to meeting the beautiful witch
def path_choice_4():
    print("You keep walking on what you think is the path, you are not sure.")
    print("It doesn't seem like anyone has been here for years")
    print("the roots of the trees are everywhere.")
    print("All of a sudden you see an old owl sitting on a branch.")
    print("It clears its throat and says:") 
    print("Hello there brave one, I've been waiting for you!")
    print("The owl continues: To get to the end you must be even braver,") 
    print("do you want to go left or forward?")
    choice = input("> ")
    if choice == 'l':
        clearConsole()
        meet_witch()
    elif choice == 'f':
        print("The trees grow too dense here, you can't get through")
        print("You have to take another path")
        print("Choose 'l' to go left")
        choice = input ("> ")
        if choice == 'l':
            clearConsole()
            meet_witch()
        else:
            print("Invalid choice, please type 'l' to keep going")
            if choice == 'l':
                clearConsole()
                meet_witch()
            else:
                path_choice_4()
        clearConsole()
    else:
        print("Invalid choice, please type 'left' or 'forward'")
        path_choice_4()
        return

# Function that introduce the witch, here the player is given an item that must be collected to 
# keep going. The player must have the "Book of wisdom" and "Badge of honor" to proceed to the Wizard.
def meet_witch():
    player_inventory = []
    print("A beautiful woman appears")
    print("Ah the trees and the gnomes were right, the witch says with a soft smile")
    print("There is a human here, I've been looking all over for you")
    print("I need to tell you something, a few words of wisdom to keep in mind")
    print("You ready? Okay, listen closely")
    print("The greatest glory in living lies not in never falling, but in rising every time we fall")
    print("You need to remember this for the rest of your journey, okay?")
    print("Matter of fact, take this book, it is filled with knowledge")
    player_inventory.append("Book of Wisdom")
    print("You have collected the book of wisdom. It has been added to your inventory")
    print("Suddenly the beautiful witch disapears and you're all alone")
    print("Where do you want to go now? Left or forward?")
    print("Enter 'l' to go left or enter 'f' to go forward!")
    choice = input("> ")
    if choice == 'l':
        if "Book of Wisdom" in player_inventory and "Badge of Honor" in player_inventory:
            print("You cannot choose 'l', you have to take 'f'")
            clearConsole()
            meet_witch()
        else:
            path_choice_3()
    elif choice == 'f':
        if "Book of Wisdom" in player_inventory and "Badge of Honor" in player_inventory:
            clearConsole()
            meet_wizard()
        else:
            print("You are not ready to go there yet, try another way.")
            choice = input("Enter 'l' to go to the left")
            if choice == 'l':
                clearConsole()
                path_choice_3()
            else:
                print("Invalid choice, please type 'l' or 'f'")
            return

# Function that introduces the Wizard, if the player give away the treasure that was collected during
# the riddle encounter the Wizard will help the player to reach the end of the forest, if
# not the wizard says something rude and disapears
def meet_wizard():
    print("You come across a wizard in the forest.")
    print("Wizard: \"A human? In here? I havent seen any of your kind in a while\"")
    print("Wizard: \"Well, most of you look like goblins, but you don't smell as foul\" He says with a smirk.")
    print("Wizard: \"I've been looking for my treasure for days! Have you seen it?\"")
    print("1. Yes, here it is.")
    print("2. No, I've never seen it.")
    choice = input("What would you like to do? ")
    if choice == "1":
        print("Wizard: \"Ah, thank you! As a reward, I will teleport you to the end of the forest.\"")
        clearConsole()
        complete_game()
    elif choice == "2":
        print("Wizard: \"Good luck getting over the stream over there by yourself, you bafoon!\"")
        print("The wizard grunts and disappears in a puff of smoke.")
        clearConsole()
        wild_stream()

# The player encounters the wild stream and has to decide how to get over it
def wild_stream():
    print("You come across a wild stream. What will you do?")
    print("1. Swim over")
    print("2. Jump over")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("You swim over the wild stream and make it safely to the other side.")
        clearConsole()
        complete_game()
    elif choice == "2":
        print("You jump over the wild stream and make it safely to the other side.")
        clearConsole()
        complete_game()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        wild_stream()

# Function that declares that the game is completed
def complete_game():
    print("You have been teleported to the end of the forest.")
    print("As you arrive, a couple of forest gnomes greet you.")
    print("'You made it!!!' 'You're alive!!!' the gnomes chant.")
    print("Well done, you made it to the other side. Go home and rest, you deserve it!")
    print("Do you want to play again? (yes or no)")
    choice = input("> ")
    if choice == "yes":
        clearConsole()
        start_game()
    elif choice == "no":
        clearConsole()
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter yes or no.")
        complete_game()

# Explains options the player has if they die
def player_death():
    global player_health
    print("You have died. You have a healing potion in your inventory, would you like to use it?")
    choice = input("> ")
    if choice == 'yes':
        player_health = 75
        print(f"You have been resurrected! Your health is now {player_health}.")
        clearConsole()
        return
    else:
        clearConsole()
        print("You have chosen not to use your healing potion. Game over.")
        game_over()
        return

# Function that declares that the game is over and gives the player a chance to start over
def game_over():
    print("This is where your story end. Do you want to try again?")
    print("Type 'y' for yes and start over or type 'n' for no and quit game")
    choice = input(">")
    if choice == 'y':
        clearConsole()
        start_game()
    elif choice == 'n':
        print("Thank you for playing and welcome back!")
        clearConsole()
    else:
        print("Invalid choice. Please enter y or n.")
        choice = input("> ")
       
start_game()