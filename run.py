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
        print("Correct! The chest is open! You collect the treasure inside! You may continue on your journey.")
        print("You have moved further into the woods")
        path_choice_2()
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
                path_choice_4()
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
            path_choice_4()
            return
        else:
            print("Invalid choice, please type 'attack' or 'run'")
            choice = input("> ")

def path_choice_2():
    print("You find yourself at another fork in the road. Do you want to go right or forward?")
    choice = input("> ")
    if choice == 'right':
        player_encounter_goblin()
    elif choice == 'forward':
        item_encounter()
    else:
        print("Invalid choice, please type 'right' or 'forward'")
        path_choice()

def item_encounter():
    items = ["A sword of fire", "A shield of ice","A ring of invisibility"]
    item = random.choice(items)
    print("You come across a chest with an item inside!")
    print(f"You found: {item}")
    global player_inventory
    player_inventory.append(item)
    print(f"you now have {player_inventory} in your inventory")
    path_choice_3()

def path_choice_3():
    print("You can barely see anything now, the light that once shined through the tree tops is now a distant memory")
    print("You sense that you are not alone, someone is watching you. But where?")
    print("You stop in your tracks, the smell of something rotten hits you!")
    print("Do you want to keep going? yes or no?")
    choice = input("> ")
    if choice == 'yes':
        player_encounter_goblin()
    else:
        print("You have no choice")
        player_encounter_goblin()
        return

def path_choice_4():
    print("Oh, wow! That was close, but you made it!")
    print("You keep walking on what you think is the path, you are not sure.")
    print("It doesn't seem like anyone has been here for years, the roots of the trees are everywhere.")
    print("All of a sudden you see an old owl sitting on a branch.")
    print("It clears its throat and says: Hello there brave one, I've been waiting for you!")
    print("The owl continues with: To get to the end you must be even braver, do you want to go left or forward?")
    choice = input("> ")
    if choice == 'left':
        riddle_encounter()
    elif choice == 'forward':
        item_encounter()
    else:
        print("Invalid choice, please type 'left' or 'forward'")

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
        complete_game()
    elif choice == "2":
        print("Wizard: \"Good luck getting over the stream over there by yourself, you bafoon!\"")
        print("The wizard grunts and disappears in a puff of smoke.")
        wild_stream()

def wild_stream():
    print("You come across a wild stream. What will you do?")
    print("1. Swim over")
    print("2. Jump over")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("You swim over the wild stream and make it safely to the other side.")
    elif choice == "2":
        print("You jump over the wild stream and make it safely to the other side.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        wild_stream()

def complete_game():
    print("You have been teleported to the end of the forest.")
    print("As you arrive, a couple of forest gnomes greet you.")
    print("'You made it!!!' 'You're alive!!!' the gnomes chant.")
    print("Well done, you made it to the other side. Go home and rest, you deserve it!")
    again = input("Do you want to play again? (yes or no)")
    if again == "yes":
        start_game()
    elif again == "no":
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter yes or no.")
        teleport()
    
# Explains options the player has if they die
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