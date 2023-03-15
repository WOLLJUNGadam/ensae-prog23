# On réalise ici les tests demandés pour la question 10 
# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file
from time import perf_counter

X = range(1,11)
data_path = "input/"
tps_total = []
nbr_tests = 10

for i in X:
    print(i)
    tps = 0
    file_name = f"network.{i}.in"
    g = graph_from_file(data_path + file_name)
    routes = f"routes.{i}.in"
    with open(data_path + routes, "r") as file:
        L = file.readlines()#On transforme le tableau en une liste de chaîne de caractères, avec une chaîne = une ligne 
        lignes=[] 
        n = int(L[0])
        for m in range(1,nbr_tests + 1): 
            lignes.append(L[m].split())
        for k in range(1,nbr_tests):
            paths = lignes[k]
            tps_debut = perf_counter()
            g.min_power(int(paths[0]), int(paths[1]))
            tps_fin = perf_counter()
            tps += tps_fin - tps_debut
        tps = (tps * n) / nbr_tests
        tps_total.append(tps)
        print(tps_total)

print(tps_total)


"""
Quelques remarques sur ce programme.
Lorque que l'on execute ce programme dans le terminal, on reçoit cette réponse :
python delivery_network/testsq10.py
1
[0.01896183800000005]
2
[0.01896183800000005, 57411.62583000001]
[0.01896183800000005, 57411.62583000001]
3
zsh: segmentation fault  python delivery_network/testsq10.py


Ainsi on remarque que le programme fonctionne pour la network.1 et le network.2, mais ensuite il y a un problème de segmentation.
Or ce problème est indépendant du nombre de tests que l'on effectue dans ce programme.
Cependant cela nous donne déjà une bonne première approximation du temps de calcul de nos algorithmes sur des fichiers avec 
beaucoup de routes et beaucoup de points. Il faudrait environ 16 heures pour effectuer tous les calculs de min_power pour le 
fichier network.2. Cela représente beaucoup de temps et ce temps de calcul est sera certainement beaucoup plus élevé pour les 
fichiers network.i (avec i appartenant de 3 à 10)

"""