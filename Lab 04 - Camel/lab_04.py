
def main():
    print("You are now running away for your life, use your time sparingly!")

    raiders = -20
    camel = 0
    thirst = 5
    done = False

    while raiders <= camel < 100 and thirst > 0 and not done:

        # constant resources being depleted / getting gained on
        distance = 0
        thirst -= 1
        raiders += 9

        # Question that gets repeated
        choice = input("What would like to do?"
                       "\nA. Rest"
                       "\nB. Drink"
                       "\nC. Travel"
                       "\nD. Travel FASTER"
                       "\nE. Quit"
                       "\n"
                       "\n")
        if choice.upper() == "A":
            print("You took a nice nap.\n")

        elif choice.upper() == "B":
            thirst += 3
            print("You feel refreshed.\n")

        elif choice.upper() == "C":
            distance += 8
            camel += 8
            print("You traveled " + str(distance) + " miles! Damn that's slow...\n")

        elif choice.upper() == "D":
            distance += 14
            camel += 14
            print("SPEEEEEEEEEEEEEEEEED! You went " + str(distance) + " miles.\n")

        elif choice.upper() == "E":
            done = True

        else:
            print("You just wasted time\n")

        # Checking to make sure you don't die / get caught by raiders or quit the game
        if done:
            print("Bye-bye!")

        elif not camel < 100:
            print("You made it to the end, good job!")

        elif not thirst > 0:
            print("You died of dehydration :(")

        elif not raiders <= camel:
            print("The raiders caught up to you, GG!")

        else:
            print("The raiders are now " + str(camel - raiders) + " miles away from you.")


main()
