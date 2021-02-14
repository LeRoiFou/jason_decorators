"""
Formation Vidéo : Les décorateurs
Lien : https://www.youtube.com/watch?v=LiBsVCXAgXI&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8&index=4

Par principe chaque fonction a une seule instruction, un decorateur prend en charge des instructions communes à
plusieurs autres fonctions

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""


def decorator(func):
    """La fonction décorator() prend en paramètre une autre fonction qui fait l'objet d'un return dans le bloc
    d'instructions """
    print('-' * 20)
    return func


@decorator
def hello():
    """La fonction decorator() est en mode property dans cette fonction ce qui permet, avant d'afficher l'instruction
    suivante dans la console, d'exécuter les instructions de la fonction decorator()"""
    print('Salut !')


def hi():
    print('Hi !')


hello()
hi()
