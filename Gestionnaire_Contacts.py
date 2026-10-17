import json

FICHIER = "contacts.json"
contacts = []


# Charger les contacts au démarrage
def charger_contacts():
    global contacts
    try:
        with open(FICHIER, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []


# Sauvegarder les contacts
def sauvegarder_contacts():
    with open(FICHIER, "w") as f:
        json.dump(contacts, f, indent=4)


# 1. Ajouter un contact
def ajouter_contact():
    nom = input("Nom : ")
    telephone = input("Téléphone : ")
    email = input("Email : ")
    contact = {"nom": nom, "telephone": telephone, "email": email}
    contacts.append(contact)
    sauvegarder_contacts()
    print("Contact ajouté !")


# 2. Afficher tous les contacts
def afficher_contacts():
    if not contacts:
        print("Aucun contact.")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. Nom: {c['nom']} | Tel: {c['telephone']} | Email: {c['email']}")


# 3. Rechercher un contact
def rechercher_contact():
    nom_recherche = input("Rechercher un contact à partir du nom : ")
    trouves = [c for c in contacts if nom_recherche.lower() in c['nom'].lower()]
    if trouves:
        for c in trouves:
            print(f"Nom: {c['nom']} | Tel: {c['telephone']} | Email: {c['email']}")
    else:
        print("Contact non trouvé.")


# 4. Supprimer un contact
def supprimer_contact():
    nom_suppr = input("Nom du contact à supprimer : ")
    global contacts
    contacts = [c for c in contacts if c['nom'].lower() != nom_suppr.lower()]
    sauvegarder_contacts()
    print("Contact supprimé si il existait.")


# Menu principal
def menu():
    charger_contacts()
    while True:
        print("\n====== Gestionnaire de contacts ======")
        print("1. Ajouter")
        print("2. Afficher")
        print("3. Rechercher")
        print("4. Supprimer")
        print("5. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            break


menu()