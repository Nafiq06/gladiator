
import random
print("Hej! du heter gladiatorn blue och du ska strida med gladiatorn red den som vinner får byns kärlek.")
print("Just nu har ni på er svärd och tjock rustning eftersom er kejsare har sagt till er att ni kommer bli rika")
options = ("slag", "kast", "spark")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (slag, kast, spark, rock): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Det står lika!")
    elif player == "rock" and computer == "spark":
        print("Du slog din fiende 80%!")
    elif player == "paper" and computer == "slag":
        print("Du slog din fiende 60%!")
    elif player == "scissors" and computer == "kast":
        print("Du vann grattis du blev känd och rik över hela byn!")
    else:
        print("Du fölorat och blev en skämt!")

    if not input("Spela igen? (y/n): ").lower() == "y":
        running = False

print("Tack för du spelade!")
print("Now you're playing as Red gladiator and you'll brawl against gladiator blue")
print("you'll fight in the Valhallah nummer 1 you can't die if you do you'll become")
print("Towns biggest loser")
running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (slag, kast, spark, rock): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Det står lika!")
    elif player == "rock" and computer == "spark":
        print("Du slog din fiende 80%!")
    elif player == "paper" and computer == "kast":
        print("Du slog din fiende 60%!")
    elif player == "scissors" and computer == "slag":
        print("Du vann grattis!")
    else:
        print("Du fölorat och din rike bränn ner!")

    if not input("Spela igen? (y/n): ").lower() == "y":
        running = False