import sqlite3

def afficher_tables_et_attributs(base_de_donnees):
    # Établir la connexion à la base de données
    connexion = sqlite3.connect(base_de_donnees)

    # Créer un objet curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()

    # Obtenir la liste des tables dans la base de données
    curseur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = curseur.fetchall()

    # Pour chaque table, afficher le nom de la table et ses attributs
    for table in tables:
        nom_table = table[0]
        print(f"\nTable: {nom_table}")

        # Obtenir la liste des attributs de la table
        curseur.execute(f"PRAGMA table_info({nom_table});")
        attributs = curseur.fetchall()

        # Afficher le nom de chaque attribut
        for attribut in attributs:
            print(f"  - {attribut[1]}")

    # Fermer la connexion
    connexion.close()

    # Remplacez "nom_de_ta_base_de_donnees.db" par le nom de votre base de données SQLite
base_de_donnees = "db.sqlite3"
afficher_tables_et_attributs(base_de_donnees)