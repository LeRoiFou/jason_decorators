"""
Formation Vidéo : Les décorateurs
Lien : https://www.youtube.com/watch?v=LiBsVCXAgXI&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8&index=4

Par principe chaque fonction a une seule utilité, un decorateur peut avoir plusieurs fonctionnalités :
-> prendre en charge des instructions communes à plusieurs autres fonctions qui ont déjà une utilité
-> imposer des conditions dans les valeurs et dans ce cas on se retrouve dans la situation d'encapsulation
des attributs d'une classe (propriétés)

La difficulté réside dans sa syntax

POURQUOI CA NE MARCHE PAS ?!? -> pour Python par principe tout est public, mettre en place des propriétés dans Python
est très compliqué, il préférable de ne pas recourir à l'encapsulation... et d'autre part peu du tutos évoquent
le principe d'encapsulation sur Python par rapport à Java...

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""

class Player:

	def __init__(self, name):
		self._name = name

	@property
	def get_name(self):
		print('test')
		return self._name

	@get_name.setter
	def get_name(self, name):
		if len(name) <= 5 :
			self._name = name
		else:
			print("Nom incorrect (5 caractères max.)")


player1 = Player("Johnssdsd")
player1.name = 'sdfdmlkjkqsdfdmlqsjkfmlfj'
print(player1.name)