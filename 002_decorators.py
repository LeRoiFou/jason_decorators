"""
Formation Vidéo : Les décorateurs
Lien : https://www.youtube.com/watch?v=LiBsVCXAgXI&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8&index=4

Par principe chaque fonction a une seule instruction, un decorateur prend en charge des instructions communes à
plusieurs autres fonctions

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""

user_logged = False  # membre non connecté


def check_user_logged(func):
    def wrapper():
        if user_logged:
            return func()
        else:
            print('Vous devez être connecté')

    return wrapper


@check_user_logged
def profil():
    print('Le profil membre...')  # cette instruction ne s'affiche pas car le membre n'est pas connecté


@check_user_logged
def articles():
    print('Les articles...')  # cette instruction ne s'affiche pas car le membre n'est pas connecté


profil()
articles()
