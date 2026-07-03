# Backend-Web-Scraping-Take-Home-Test
# Product Scraper Script

Ce script Python permet d'extraire des informations produits (socks) depuis un index Algolia via une requête POST et de les sauvegarder dans un fichier JSON.

Site = https://www.salomon.com/accessories/socks

API = 
https://k1n6gb06ip-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(5.46.0)%3B%20Lite%20(5.46.0)%3B%20Browser%3B%20instantsearch.js%20(4.86.1)%3B%20react%20(19.3.0-canary-f93b9fd4-20251217)%3B%20react-instantsearch%20(7.22.1)%3B%20react-instantsearch-core%20(7.22.1)%3B%20next.js%20(16.1.6)%3B%20JS%20Helper%20(3.27.0)&x-algolia-api-key=ZGExZGNkYWNlMzY1YzAwNWUyNTEwY2FkMDMzN2IzMDc4MTQzZmNlZTJmNWI4NGI3ODU0Nzc3MWE1M2NjNDZkM2ZpbHRlcnM9Tk9UJTIwbm90VmlzaWJsZUJ5UmVhc29uQ29kZSUzQUQyQyZydWxlQ29udGV4dHM9cmVhc29uQ29kZS1EMkMmdXNlclRva2VuPTE2Zjk5NWIxLThiYWEtNDAyMy1iY2QyLWM3ZDk4YTE2YzI2OSZ2YWxpZFVudGlsPTE3NzAwMDE0ODg%3D&x-algolia-application-id=K1N6GB06IP 

---

## Fonctionnalités

- Requête vers l'API Algolia pour récupérer les produits.
- Extraction des informations clés de chaque produit :
  - Nom du produit (`modelName`)
  - URL de l’image (`imageUrl`)
  - Référence/modèle (`modelCode`)
  - Prix (`price`)
  - Disponibilité (`isInStock`)
  - URL du produit (`url`)
  - Étiquette/condition (`label`)
  - Pourcentage de stock (`inStockPercentage`)
- Affichage des informations produit ligne par ligne dans la console.
- Sauvegarde de toutes les données extraites dans un fichier `products.json`.

---

## Prérequis

- Python 3.8 ou supérieur
- Modules Python nécessaires :
  - `requests`
  - `json` (inclus dans Python standard)

Pour installer `requests` : pip install requests


## Structure du code

Constantes :

URL : URL de l'API Algolia.

HEADERS : En-têtes HTTP nécessaires pour la requête (incluant clé API et User-Agent).

DATA : Payload JSON pour la requête POST vers Algolia.

Fonctions utilitaires :

extract_price(hit) : Récupère le prix du produit depuis la réponse, que ce soit sous forme de dict ou valeur directe.

extract_label(hit) : Récupère l’étiquette ou condition du produit s’il y en a.

Fonction principale (main) :

Envoie la requête POST à l’API.

Vérifie le statut de la réponse.

Parcourt les résultats pour extraire les informations produit.

Affiche chaque produit dans la console.

Sauvegarde tous les produits dans products.json.

## Utilisation

Ouvrir l’invite de commandes Windows (CMD).

Télécharger le script algolia_request.py.

Se placer dans le dossier contenant le script algolia_request.py : cd C:\Chemin\Vers\Le\Dossier

Installer la dépendance requests si ce n’est pas déjà fait : pip install requests

Lancer le script avec Python : python algolia_request.py


Après exécution :

Les informations de chaque produit s’affichent dans la console.

Toutes les données sont sauvegardées dans le fichier products.json à la racine du projet.
