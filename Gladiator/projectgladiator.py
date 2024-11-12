# # Steg 1: Skapa en meny där spelaren får välja om det ska finnas blodiag beskrivningar i spelet eller inte
# # Steg 2: Lägga in nya printsatser med blodiag beskrivningar när någon blir träffad och skadad
# # Steg 3: Göra så att dessa beskrivningar bara visas som blod är påslaget
# # (Steg 4: Gör så att det finns flera beskrvinbingar och att spelet slumpar vilken som ska visas)



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

print("now you're playing as gladiator red and you're gonna fight against gladiator blue how will you suvive")
options = ("punch", "jab", "grab")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (punch, jab, grab): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "punch" and computer == "grab":
        print("You win!")
    elif player == "jab" and computer == "punch":
        print("You win!")
    elif player == "grab" and computer == "jab":
        print("You won and earned the villigers trust and earned their respect!!")
    else:
        print("You died!")

    if not input("Spela igen? (y/n): ").lower() == "y":
        running = False

    
 












