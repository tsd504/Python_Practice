import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    print_slow("You are an astronaut exploring a deserted spaceship.")
    print_slow("Unknown to you, there are a number of infected astronauts still aboard the ship.")
    print_slow("Your mission is to explore the ship and find out what happened.")
    print_slow("Good luck!")

def decision_one():
    print_slow("You enter the spaceship and find yourself in a dark corridor.")
    print_slow("Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print_slow("Invalid choice. Try again.")
        decision_one()

def left_path():
    print_slow("You turn left and walk down the corridor.")
    print_slow("You hear strange noises coming from a room ahead.")
    print_slow("Do you want to investigate the room or keep walking?")
    choice = input("Enter 'investigate' or 'walk': ").lower()
    if choice == 'investigate':
        investigate_room()
    elif choice == 'walk':
        keep_walking()
    else:
        print_slow("Invalid choice. Try again.")
        left_path()

def right_path():
    print_slow("You turn right and walk down the corridor.")
    print_slow("You find a control room with a computer terminal.")
    print_slow("Do you want to access the terminal or keep walking?")
    choice = input("Enter 'access' or 'walk': ").lower()
    if choice == 'access':
        access_terminal()
    elif choice == 'walk':
        keep_walking()
    else:
        print_slow("Invalid choice. Try again.")
        right_path()

def investigate_room():
    print_slow("You enter the room and find an infected astronaut!")
    print_slow("The astronaut attacks you and you have no choice but to fight.")
    print_slow("You manage to defeat the astronaut but you are injured.")
    print_slow("You need to find a medkit to heal yourself.")
    find_medkit()

def keep_walking():
    print_slow("You keep walking down the corridor.")
    print_slow("You find a medkit on the floor and use it to heal yourself.")
    print_slow("You continue exploring the spaceship.")
    decision_two()

def access_terminal():
    print_slow("You access the terminal and find logs about the infection.")
    print_slow("You learn that the infection spreads through physical contact.")
    print_slow("You need to find a way to contain the infection and escape the spaceship.")
    decision_two()

def find_medkit():
    print_slow("You search the spaceship for a medkit.")
    print_slow("You find a medkit in the medical bay and use it to heal yourself.")
    print_slow("You continue exploring the spaceship.")
    decision_two()

def decision_two():
    print_slow("You reach a junction with three paths.")
    print_slow("Do you want to go left, right, or straight?")
    choice = input("Enter 'left', 'right', or 'straight': ").lower()
    if choice == 'left':
        left_path_two()
    elif choice == 'right':
        right_path_two()
    elif choice == 'straight':
        straight_path()
    else:
        print_slow("Invalid choice. Try again.")
        decision_two()

def left_path_two():
    print_slow("You turn left and find a room with more infected astronauts.")
    print_slow("You decide to avoid the room and go back to the junction.")
    decision_two()

def right_path_two():
    print_slow("You turn right and find an escape pod.")
    print_slow("Do you want to use the escape pod or keep exploring?")
    choice = input("Enter 'use' or 'explore': ").lower()
    if choice == 'use':
        use_escape_pod()
    elif choice == 'explore':
        decision_two()
    else:
        print_slow("Invalid choice. Try again.")
        right_path_two()

def straight_path():
    print_slow("You go straight and find the source of the infection.")
    print_slow("You manage to contain the infection and save the spaceship.")
    print_slow("Congratulations! You have completed your mission.")

def use_escape_pod():
    print_slow("You use the escape pod and leave the spaceship.")
    print_slow("You have escaped safely but the infection is still on the spaceship.")
    print_slow("Mission failed.")

def main():
    intro()
    decision_one()

main()