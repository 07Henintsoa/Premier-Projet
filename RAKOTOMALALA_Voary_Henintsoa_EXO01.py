#Affichage de la table de verite
def tableau_verite(variables, expression):
    nombre_de_ligne = 2**len(variables)
    premiere_ligne = " | ".join(variables)
    presentation = "".join(variables)
    print(premiere_ligne + " |f({})".format(presentation))
    print("-"*70)
    maxtermes = []
    mintermes = []
    for w in range(nombre_de_ligne):
        ligne = []
        binaire = bin(w)[2:].zfill(len(variables))
        ligne.extend(list(binaire))
        solution = kajikajy(variables, binaire, expression)
        ligne.append(str(int(solution)))
        print(" | ".join(ligne))
        composee = "+".join(variables)
        for m in range(len(variables)):
            if int(binaire[m]) == 0:
                prime = "{}'".format(variables[m])
                composee = composee.replace(variables[m], prime)
#Triage des mintermes et des maxtermes pour afficher les formes canoniques 
        f = int(solution)
        if f == 1:
            y = composee.split("+")
            composee = "".join(y)
            maxtermes.append(composee)
        else:
            mintermes.append(composee)
    dfc = ")*(".join(mintermes)
    print("la premiere forme canonique est : f = ", "+".join(maxtermes))
    print("et la deuxieme forme canonique est : g = ({})".format(dfc))

#Calcul de la fonction dont l'utilisateur a saisie
def kajikajy(variables, binaire, expression):
    stockage_var = {variables[k]: int(binaire[k]) for k in range(len(variables))}
    for var, val in stockage_var.items():
        expression = expression.replace(var, str(val))
    return eval(expression)

#programme principale 
variables = []
print("Ce programme a ete fait par : \n Nom = RAKOTOMALALA \n Prenoms = Voary Henintsoa \n N° d'inscription = UA03230FS2024 \n Grade = L1 \n Mathematiques et Infomatique")
print()
print()
print("De preference , ne pas utiliser les lettres minuscules 'a' , 'n', 'd', 'o' et 'r \n Et pour moin de confusions veuillez utiliser les parentheses \nLes operateurs que vous utiliserez dans ce programme sont : 'and' , 'or' et 'not'")
n = int(input("Entrer le nombre de variables que vous comptez utiliser: "))
for i in range(0, n, 1):
    xi = str(input("entrer la variables {}: ".format(i+1)))
    variables.append(xi)
expression = input("Entrez la fonction logique : ")
table = tableau_verite(variables, expression)
