n = int(input("Saisir le Nombre des Elements : "))
List = []
for i in range(n):
    x = int(input("Saisir le {}eme Element : ".format(i+1)))
    List.append(x)

x = int(input("Saisir le Nombre pour Chercher : "))

chercher = False

for i in List:
    if i == x:
        chercher = True
        break

print(chercher)
