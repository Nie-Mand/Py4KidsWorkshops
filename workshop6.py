n = int(input("Saisir le Nombre des Elements : "))
List = []
for i in range(n):
    x = int(input("Saisir le {}eme Element : ".format(i+1)))
    List.append(x)

x = int(input("Saisir le Nombre pour Chercher : "))

right = n-1
left = 0
while left <= right :
    if right == left :
        chercher = (x == List[right])
        break
    else :
        middle = (left + right) // 2
        if x > List[middle] :
            left = middle+1
        else :
            right = middle-1

print(chercher)
