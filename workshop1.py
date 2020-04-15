print("Bienvenue Dans Notre Formulaire")

nom = input("Nom : ")
prenom = input("Prenom : ")
stars = int(input("Ton Evaluation : "))
pourquoi = input("Pourquoi tu veux nous Evalue? ")
plus = input("Tu as Quelque Chose pour dire? ")

nom_complet = nom + " " + prenom

feedback = "Bonjour, je suis {}, je vous donne {} STARS car {}. {}"

print(feedback.format(nom_complet, stars, pourquoi, plus))


