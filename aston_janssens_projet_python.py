print("------------ Bienvenu dans votre programme de comptage de billets ------------")

# La classe regroupe un ensemble de variables (= attributs) et de fonctions (= méthodes)
# Le paramètre self permet de faire appel plus facilement plus tard aux attributs

class employee(object):

    # Le init est un constructeur et permet d'initier les attributs de la classe
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # étape permettant de récupérer le nom de l'employé
    def getName(self):
        return self.name

    # étape permettant de récupérer le salaire de l'employé
    def getSalary(self):
        return self.salary


# num rest correspond au nombre d'employés restant à encoder
# go_on permet de dire à la machine "tant que cette variable vaut true , on continue la boucle et si elle
# est false, on arrête la boucle
# le tableau vide permet par la suite d'aller y encoder des données
table_emp_sal = []
num_rest = 0
go_on = True


# fonction permettant d'encoder les données de maximum 10 employés (salaires, noms)

#tant que le nb d'employés restants est inférieur à 10, et que go on = true, on continue la boucle
# et on demande d'encoder le nom d'abord + on définit que le salaire est de 0 à la base
while num_rest < 10 and go_on == True:
    name = input(
        '******************************************************************************************************************************************************************************************************************************************************************************************************\n'
        'Votre Nom : \n')
    salary = 0

# permet de définir que le salaire doit se situer entre 10 et 5000 et qu'il correspond à un nombre float (+ réel positif)
# il y a également une fonction permettant d'ajouter l'information encodée dans le tableau (vide à la base)
    while salary < 10 or salary >= 5000:
        salary = float(input('Introduisez un salaire se situant entre 10€ et 5000€ : \n'))
        print(
            '*********************************************************************************************************************************************************************************************************************************************************************************************************\n')
    table_emp_sal.append(employee(name, salary))

# une fois qu'on en a un encodé 1, on affiche une certaine phrase/question + si réponse oui ou non -> action spécifique
    if go_on and num_rest < 9:
        next = input('---------Vous pouvez encore ajouter ' + str(
            10 - (num_rest + 1)) + "---------" + '\n' + '---------Voulez-vous continuer ? go/stop---------' + '\n')

    if next == 'stop':
        go_on = False

    if next == 'go':
        go_on = True

# à la fin, on ajoute 1 au nombre d'employés restants
    num_rest += 1



# fonction de comptage de billets sur base d'un salaire float


# assignation du nombre de coupure par coupure (par défaut il y a 0 unité pour chaque type de billets)
# cela permettra de calculer le nombre final de billets nécessaires (à aller chercher à la banque)
total_notes = {
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0,
    0.5: 0,
    0.1: 0,
    0.05: 0,
    0.02: 0,
    0.01: 0
}

#Cette fonction permet de compter le nombre de billets/pièces nécessaires pour composer un salaire
def count_currency(salary):
#un tableau reprenant les différents types de billets ou de pièces, chacun ayant une position spécifique
    notes = [
        200, 100, 50, 20,
        10, 5, 2, 1, 0.5,
        0.10, 0.05, 0.02, 0.01
    ]
#un tableau permettant de comptabilisé combien il faut de billets de chaque type
    note_counter = [0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0, ]
#une boucle permettant de calculer le nombre de billets nécessaires pour le salaire
#zip permet de créer une nouvelle entité (équivalent d'un dictionnaire) sur pase de 2 itérables (notes + note_counter)
#i =notes et j= note_counter
    for i, j in zip(notes, note_counter):
        if salary >= i:
            #si le salaire est plus grand que la référence billet (ex: 200€), alors j vaut le salaire divisé par i et
            #on prend note du reste
            j = salary // i
            salary = salary - j * i
            #le salaire à ce moment vaut le salaire de base - la référence billet * le nombre de références billets
            total_notes[i] += j
            # on encode le nombre de billets de chaque type dans le tableau de comptage final
            # on affiche le nombre de billets pour chaque type de billets
            print("{} * {}".format(int(j), i))


# la suite permet de parcourir tout le tableau avec les données qui y sont encodées
# range défini la portée dans laquelle se trouve l'info, ici l'info se trouve au maximum dans le tableau
# pour l'élément i dans le tableau, on applique la boucle (i vaut les différents valeurs des billets/pièces)
for i in range(len(table_emp_sal)):
    # récupération du nom du salarié courant (avec get) dans le tableau
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Le nombre de billets ou pièces nécessaires pour Mr/M {}:".format(table_emp_sal[i].getName()))
    # permet d'afficher le nombres de billets pour le salaire pour chaque personne
    count_currency(table_emp_sal[i].getSalary())
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print(
    "**********************************************************************************************************************************************************************************************************************************************************************************************************"
    "\n\nIl faudra aller chercher au final le nombre de billets et de pièces suivant;\n")
# boucle clé: valeur pour chaque élement du dictionnaire
# pour les éléments k (valeurs des billets et pièces) et v (nombre de chaque billets/pièces) dans les items du tableau final
for k, v in total_notes.items():
    # permet d'afficher la valeur si elle est non-nulle (si elle est nulle on affiche donc pas)
    # affiche les valeurs du tableau qui a comptabilisé l'ensemble des billets durant tout le programme
    if (v != 0):
        print("{} * {}".format(k, v))

print(
    "**********************************************************************************************************************************************************************************************************************************************************************************************************'\n'")

print("------------ Fin du programme de comptage de billets, aurevoir! ------------")