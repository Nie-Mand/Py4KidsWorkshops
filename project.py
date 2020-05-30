mdp = input("Saisissez le mot de passe : ")
livres = []
if mdp == "Python4Kidz" :
    while True :
        print("Qu'est-ce que tu veux faire ? [ajouter un livre : 1, acheter un livre : 2]")
        choix = int(input("Votre choix : "))
        if choix == 1 :
            id = input("Identifiant : ")
            nom = input("Nom : ")
            auteur = input("Auteur : ")
            editeur = input("Editeur : ")
            anneepub = input("Annee de Publication : ")
            categorie = input("Catégorie : ")
            livre = {"id":id, "nom":nom, "auteur":auteur, "editeur":editeur, "anneepub":anneepub, "categorie":categorie, "disponible": True}
            livres.append(livre)
        else :
            choix = input("Que recherchez-vous: [catégorie - auteur] : ")
            if choix == "catégorie" :
                categorie = input("Saisissez la catégorie : ")
                for livre in livres :
                    if livre["categorie"] == categorie :
                        print(livre["id"], livre["nom"], livre["auteur"], livre["editeur"], livre["anneepub"], livre["categorie"])
            else :
                auteur = input("Saisissez le nom d'auteur : ")
                for livre in livres :
                    if livre["auteur"] == auteur :
                        print(livre["id"], livre["nom"], livre["auteur"], livre["editeur"], livre["anneepub"], livre["categorie"])
            id = input("Saisissez l'identifiant : ")
            for i in range(len(livres)) :
                if livres[i]["id"] == id :
                    if livres[i]["disponible"] == False :
                        print("le livre est indisponible")
                    else :
                        print("merci d'avoir acheté chez nous")
                        livres[i]["disponible"] = False
                    break

