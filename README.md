# OCR_P4 - Projet P7 - R�solvez des probl�mes en utilisant des algorithmes en Python
### Algorithmes d�velopp�s pour la soci�t� AlgoInvest&Trade
***
## Pr�sentation


A �t� demand�, la r�alisation d'un algorithme de force brute et d'un algorithme optimis� pour calculer le meilleur investissment possible � travers l'achat d'actions

***
## Pr�requis : 
[![made-with-python](
https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](
https://www.python.org/)
[![Python badge](https://img.shields.io/badge/Python->=3.9.9-blue.svg)](
https://www.python.org/)
***
## Clonage du Repository :
````shell
git clone https://github.com/clsayart/projetOC7
````
***
## Environnement Virtuel :
cr�ation de l'environnement virtuel
```shell
python3 -m venv [nom_de_votre_environnement_virtuel] 
```
activation de l'environnement virtuel
### Mac/Linux
````shell
source [nom_de_votre_environnement_virtuel]/bin/activate
````
### Windows
````shell
[nom_de_votre_environnement_virtuel]\Scripts\activate
````

Aller dans le dossier pythonProject7 contenant les fichiers
```shell
cd pythonProject7 
```
***
## Installation des packages n�cessaires
````shell
pip install -r requirements.txt 
````
***
## Lancement du programme : 
Ex�cution des algorithmes via 2 fichiers:
````shell
python3 bruteforce.py 
````
````shell
python3 optimized.py 
````
Cette commande produit le resultat suivant : 

Cr�ation d'un fichier .txt dans le dossier Results avec le meilleur investissment


 ###G�n�ration Rapport Flake8

Apr�s avoir activ� l'environnement virtuel, entrez la commande suivante:

```shell
flake8 --format=html --htmldir=flake_rapport

flake8 --format=html --htmldir=flake_rapport --exclude venv

```
Un rapport sera g�n�r� dans le dossier "flake_rapport", avec comme argument 
"max-line-length" d�fini par d�faut � 79 caract�res par ligne si non pr�cis�.
