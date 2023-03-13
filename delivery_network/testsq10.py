# On réalise ici les tests demandés pour la question 10 
# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file
from time import perf_counter

X = range(1,3)
data_path = "input/"
tps_total = []
nbr_tests = 20

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
