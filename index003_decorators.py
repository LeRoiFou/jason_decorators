"""
Formation Vidéo : Les décorateurs
Lien : https://www.youtube.com/watch?v=LiBsVCXAgXI&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8&index=4

Par principe chaque fonction a une seule utilité, un decorateur peut avoir plusieurs fonctionnalités :
-> prendre en charge des instructions communes à plusieurs autres fonctions qui ont déjà une utilité
-> imposer des conditions dans les valeurs et dans ce cas on se retrouve dans la situation d'encapsulation
des attributs d'une classe (propriétés)

La difficulté réside dans sa syntax

Cet fois-ci on paramètre le décorateur

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""

user_name = "John"


def check_user(username):
	def decorator(func):
		def wrapper():
			if username == user_name:
				return func()
			else:
				print("Utilisateur inconnu")
		return wrapper
	return decorator


@check_user("Jo")
def profil():
    print('Le profil membre...')  # cette instruction ne s'affiche pas car le membre n'est pas connecté

profil()
