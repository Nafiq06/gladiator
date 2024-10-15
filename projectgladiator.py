
import random
print("Hej! du heter gladiatorn blue och du ska strida med gladiatorn red den som vinner får byns kärlek.")
print("Just nu har ni på er svärd och tjock rustning eftersom er kejsare har sagt till er att ni kommer bli rika")


options = ("spark", "slag", "kast")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (spark, slag, kast): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "spark" and computer == "kast":
        print("You win!")
    elif player == "slag" and computer == "spark":
        print("You win!")
    elif player == "kast" and computer == "slag":
        print("Du vann och blev känd över hela riket!")
    else:
        print("Du dog!")

    if not input("Spela igen? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")