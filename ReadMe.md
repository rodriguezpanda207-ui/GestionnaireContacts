📞 Gestionnaire de Contacts JSON

Un programme en ligne de commande développé en Python pour gérer efficacement un carnet d'adresses avec sauvegarde automatique dans un fichier JSON.

✨ Fonctionnalités

➕ Ajouter un contact : Enregistrement du nom, téléphone et adresse email.

📋 Afficher les contacts : Consultation de la liste complète des contacts enregistrés.

🔍 Rechercher un contact : Recherche par nom (insensible à la casse).

❌ Supprimer un contact : Retrait d'un contact de la liste.

💾 Persistence des données : Sauvegarde et chargement automatiques dans le fichier contacts.json.

🛠️ Prérequis

Python 3.12 (ou toute version de Python 3.x).

Aucune bibliothèque externe n'est requise (utilisation du module natif json).

📦 Installation & Lancement

Cloner le dépôt (ou télécharger les fichiers) :

git clone https://github.com/votre-nom-utilisateur/gestionnaire-contacts.git
cd gestionnaire-contacts


Lancer le programme :

python main.py


(Assure-toi de remplacer main.py par le nom exact de ton fichier .py si besoin).

📁 Structure des Données

Les contacts sont sauvegardés au format JSON dans un fichier contacts.json à la racine du projet :

[
    {
        "nom": "Panda Rodriguez",
        "WhatsApp": "+229 0192782988",
        "email": "rodriguezpanda207@gmail.com"
    }
]


👤 Auteur



Projet développé dans le cadre d'un apprentissage Python & Git/GitHub.