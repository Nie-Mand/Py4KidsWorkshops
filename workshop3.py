import random

minimum = int(input("Saisir le Minimum : "))
maximum = int(input("Saisir le Maximum : "))

guessed = random.randint(minimum, maximum)

user = int(input("Devinez le nombre : "))

tries = 1

while user != guessed :
    tries += 1
    if user > guessed :
        print("Non, Essayez un Nombre plus petit")
    else :
        print("Non, Essayez un Nombre plus grand")
    user = int(input("Devinez le nombre : "))

if tries <= 3 :
    print(f"Felicitation! Tu Essais {tries} Fois")
elif tries >= 6 and tries > 3:
    print(f"Pas Mal, Tu Essais {tries} Fois")
else:
    print(f"Dommage, Tu Essais {tries} Fois")
