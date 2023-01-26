import random

# Global variables
player_health = 75
player_attack = 10
player_defense = 6
player_inventory = ["A healing potion"]

def start_game():
    # Introduction and initial setup
    print("Welcome to the this adventure game! You are about to embark on an epic journey filled with challenges and mysterious obstacles. Your goal is to complete each task so that you can reach your village on the other side of the woods. Are you ready for the adventure of a lifetime? ")
    player_name = input("What is your name? ")
    print(f"Welcome {player_name} to the Damned Willow Forest! You find yourself standing at the dense growing trees, wondering how you will get by. As you look ahead, you notice a signpost that lists several tasks that must be completed before you can continue on your journey. The tasks you must complete will test your skills and determination so you can get home. Are you ready? Take a deep breath, and let the adventure begin!")
    choice = input("Are you ready to continue? Type 'yes' or 'no': ")
    if choice == 'yes':
        print(f"Here is some valid information about your character: \n Health: {player_health}\n Attack: {player_attack}\n Defense: {player_defense}\n Inventory: {player_inventory}\n")
        input("Press any key to enter the woods: ")
        path_choice()
    else:
        print("Thanks for playing! Have a good day!")
        return

# Display the different path choices
def path_choice():
    print("You find yourself at a fork in the road. Do you want to go left or right?")
    choice = input("> ")
    if choice == 'left':
        riddle_encounter()
    elif choice == 'right':
        player_encounter_goblin()
    else:
        print("Invalid choice, please type 'left' or 'right'")
        path_choice()

# solve the riddle
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
        print("Correct! The chest is open! You collect the treasure inside! You may continue on your journey.")
        return
    else:
        print("Incorrect. You have failed the task.")
        player_death()

# Fight the enemy
def player_encounter_goblin():
    goblin_health = 45
    goblin_attack = 18

    print("You have come across a nasty forest goblin!")
    choice = input("Do you want to attack or run? ")

    while goblin_health > 0:
        if choice == 'attack':
            global player_health
            player_attack = random.randint(8, 12)
            goblin_health -= player_attack
            if goblin_health <= 0:
                print("You have defeated the goblin! You may continue on your journey.")
                return
            else:
                print(f"The goblin now has {goblin_health} health.")
                player_health -= goblin_attack
                if player_health <= 0:
                    player_death()
                else:
                    print(f"You now have {player_health} health.")
                    choice = input("Do you want to attack or run? ")
        elif choice == 'run':
            print("You run away from the goblin.")
            return
        else:
            print("Invalid choice, please type 'attack' or 'run'")
            choice = input("> ")

def player_death():
    global player_health
    print("You have died. You have a healing potion in your inventory, would you like to use it?")
    choice = input("> ")
    if choice == 'yes':
        player_health = 75
        print(f"You have been resurrected! Your health is now {player_health}.")
        return
    else:
        print("You have chosen not to use your healing potion. Game over.")
        return

# Start the game
start_game()