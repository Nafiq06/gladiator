# Steg 1: Skapa en meny där spelaren får välja om det ska finnas blodiag beskrivningar i spelet eller inte
# Steg 2: Lägga in nya printsatser med blodiag beskrivningar när någon blir träffad och skadad
# Steg 3: Göra så att dessa beskrivningar bara visas som blod är påslaget
# (Steg 4: Gör så att det finns flera beskrvinbingar och att spelet slumpar vilken som ska visas)



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

    
    def main():
print('Gladiator in Python')
print()
print('Rules: 1) spear wins over whip.')
print(' 2) whip wins over sword.')
print(' 3) sword wins over spear.')




def spear_sword_whip():
guess = 'sp','s','w'
computer_score = 0
person_score = 0
rounds = 1

total_rounds= int(input("How many points does it take to win? "))


while(computer_score < total_rounds and person_score < total_rounds):
while (computer_score < total_rounds and person_score < total_rounds):
print("******************* ROUND #", rounds, "*******************")
spear_sword_whi = input("Pick your throw: [s]pear, [s]word, or [w]hip? ")
break
computer = random.choice(guess)
if spear_sword_whi == computer:
print('Tie!')
rounds +=1

elif (spear_sword_whi == 'p' and computer == 'r'):
print('Computer threw rock, you win!')
person_score=person_score+1
rounds +=1

elif (spear_sword_whi == 'r' and computer == 's'):
print('Computer threw scissors, you win!')
person_score=person_score+1
rounds +=1

elif(spear_sword_whi == 's' and computer == 'p'):
print('Computer threw paper, you win!')
person_score=person_score+1
rounds +=1

elif(spear_sword_whi == 'r' and computer == 'p'):
print('Computer threw paper, you lose!')
computer_score=computer_score+1
rounds +=1

elif (spear_sword_whi == 's' and computer == 'r'):
print('Computer threw rock, you lose!')
computer_score=computer_score+1
rounds +=1

else:
(spear_sword_whi == 'p' and computer == 's')
print('Computer threw scissors, you lose!')
computer_score=computer_score+1
rounds +=1

print ("Your score:" , person_score)
print ("Computer's score:", computer_score)

return

main()
spear_sword_whi()