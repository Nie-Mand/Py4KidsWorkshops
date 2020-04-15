choice = int(input("Tue Veux Crypter [1] ou Decrypter [2] ? "))

if choice == 1 :
    msg = input("Saisir un Message pour Crypter : ")
    key = int(input("Saisir le Cle ( Nombre ) : "))
    encrypted = ""
    for i in msg :
        if i.isalpha() : 
            x = ord(i.lower()) + key
            if x > 122 :
                x -= 26
            encrypted = encrypted + chr(x)
        else :
            encrypted = encrypted + i
    print(f"Message Cryptee est : {encrypted}")
else :
    msg = input("Saisir un Message pour Decrypter : ")
    key = int(input("Saisir le Cle ( Nombre ) : "))
    decrypted = ""
    for i in msg :
        if i.isalpha() : 
            x = ord(i.lower()) - key
            if x < 97 :
                x += 26
            decrypted = decrypted + chr(x)
        else :
            decrypted = decrypted + i

    print(f"Message DeCryptee est : {decrypted}")    

