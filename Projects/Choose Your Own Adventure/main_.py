from time import sleep
global health
death_song = "May your name live on in song..."
left = "left"
right = "right"
yes = "yes"
no = "no"

def name_input():
    name = input("What is your name traveler? ")
    print("Very well,",name,"!")

def age_input():
    global age
    try:
        age = int(input("And how many years have you wondered these lands? "))
    except:
        print("Please give me a number.")
        age_input()

def of_age():
    global health
    health = 10
    if age >= 13:
        print("Excellent! Let us begin!")
        sleep(1)
        print("You are embarking with a health value of ", str(health))
    else:
        print("Your bravery is beyond your years, but you cannot venture forth.")
        quit()

def choice1():
    global health
    sleep(1)
    first_choice = input("You've come to a fork in the road. Shall you go left or right? ")
    if first_choice.lower() != left:
        sleep(1)
        print("You were fatally attacked by a werewolf. ",death_song)
        quit()
    else:
        sleep(1)
        print("So far so good")

def choice2():
    global health
    sleep(1)
    second_choice = input("You hear running water. Do you want to find the source? ")
    if second_choice.lower() != yes:
        sleep(1)
        print("A tarantula landed on your shoulder, biting you and causing 5 health damage.")
        sleep(1)
        health = health -5
    else:
        print("A keen decision!")
        sleep(1)
        print("You found fresh water! Drink up!")
        health = health +5
        sleep(1)
        print("You've added 5 points to your health bar. This gives you " + str(health) + " health points!")
        sleep(1)
        print("Onward!")

def main():
    print("Prepare to Choose Your Destiny")
    name_input()
    age_input()
    of_age()
    choice1()
    choice2()


main()


