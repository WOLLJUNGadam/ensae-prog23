# On réalise ici les tests demandés pour la question 15 
# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, kruskal_min_power
from time import perf_counter
from math import floor

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
            kruskal_min_power(g,int(paths[0]), int(paths[1]))
            tps_fin = perf_counter()
            tps += tps_fin - tps_debut
        tps = floor(tps * n) / floor(nbr_tests)
        tps_total.append(floor(tps))
        print(tps_total)

print(tps_total)


"""
Quelques remarques sur ce programme.
Lorque que l'on execute ce programme dans le terminal, on reçoit cette réponse :
python tests/test_s2q15_kruskal_min_power.py
1
[0]
2
[0, 586]
3
[0, 586, 2570]
4
[0, 586, 2570, 2800]
5
[0, 586, 2570, 2800, 1027]
6
[0, 586, 2570, 2800, 1027, 4459]
7
[0, 586, 2570, 2800, 1027, 4459, 4206]
8
[0, 586, 2570, 2800, 1027, 4459, 4206, 4131]
9
[0, 586, 2570, 2800, 1027, 4459, 4206, 4131, 4138]
10
Traceback (most recent call last):
  File "/Users/adamwolljung/Desktop/ENSAE/1A-S2/Projet_python/ensae-prog23/tests/test_s2q15_kruskal_min_power.py", line 20, in <module>
    g = graph_from_file(data_path + file_name)
  File "/Users/adamwolljung/Desktop/ENSAE/1A-S2/Projet_python/ensae-prog23/delivery_network/graph.py", line 180, in graph_from_file
    edge = list(map(int, file.readline().split()))
ValueError: invalid literal for int() with base 10: '0.211549803713317'




Ainsi on remarque que le programme fonctionne pour tous les network sauf le network.10. La raison de cela est que les puissances
dans le network.10 ne sont pas des entiers et alors il y a une erreur avec la fonction graph-from-file. On notera qu'on va 
essayer de remplacer "edge = list(map(int, file.readline().split()))" par "edge = list(map(float, file.readline().split()))"

Cependant cela nous donne déjà une bonne première approximation du temps de calcul de notre nouvel algorithme. 
Alors qu'il nous faudrait environ 16 heures pour effectuer tous les calculs de min_power pour le fichier network.2 avec les 
algorithmes de la séance 1. Il nous faudrait maintenant 10 minutes environ afin de fairre ces calculs. Ainsi on a économisé 
beaucoup de temps, ce qui est un bon point pour l'écologie notamment, et cela va nous aider à pouvoir calculer les chemins 
pour des fichiers plus importants.

"""