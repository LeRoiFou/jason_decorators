"""
Formation Vidéo : Les décorateurs
Lien : https://www.youtube.com/watch?v=LiBsVCXAgXI&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8&index=4

Par principe chaque fonction a une seule utilité, un decorateur peut avoir plusieurs fonctionnalités :
-> prendre en charge des instructions communes à plusieurs autres fonctions qui ont déjà une utilité
-> imposer des conditions dans les valeurs et dans ce cas on se retrouve dans la situation d'encapsulation
des attributs d'une classe (propriétés)

La difficulté réside dans sa syntax

Lorsqu'on veut accéder à une explication d'une méthode/ d'une fonction dans laquelle figure un docstring,
on utilise l'instruction help(nomFonction / nomMethode)
Lorsque la méthode / fonction a un décorateur, la fonction help sera insuffisante pour accéder aux commentaires
figurant dans la méthode / fonction concernée.
À cela, il faut importer le module functools et ajouter l'instruction suivante : @functools.wraps(func) avant
la fonction qui va être utilisée en tant que décorateur

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""
import functools  # pour accéder aux commentaires de la fonction profil() ci-après qui a un décorateur

user_name = "John"


def check_user(username):
	def decorator(func):
		@functools.wraps(func)  # ajout de cette instruction pour accéder aux commentaires de la fonction profil()
		def wrapper():
			if username == user_name:
				return func()
			else:
				print("Utilisateur inconnu")
		return wrapper
	return decorator


@check_user("Jo")
def profil():
	"""
	Page d'accès au profil de l'utilisateur
	"""
	print('Le profil membre...')  # cette instruction ne s'affiche pas car le membre n'est pas connecté

help(profil)
