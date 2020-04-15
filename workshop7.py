import random
rounds = int(input("Saisir le Nombre des Tours : "))
user = 0
prog = 0
for i in range(rounds):
    u = int(input("Saisir un Nombre entre 1 et 3 [1:Pierre, 2: Papier, 3: Ciseaux] : "))
    p = random.randint(1, 3)
    print("J'ai Choisis : ", p)
    if (u == 1 and p == 3) or (u == 2 and p == 1) or (u == 3 and p == 2) :
        user = user + 1
    elif u == p :
        pass
    else :
        prog = prog + 1
print(f"Ton Score est : {user} et mon score est : {prog}")
if user > prog :
    print("Felicitations! Tu es le Gagnant!")
elif user < prog :
    print("Haha! Je Suis le Gagnant!")
else :
    print("Nulle")



