from graph import Graph, graph_from_file, kruskal, kruskal_min_power


data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)

print(g)

print(kruskal(g))

print(kruskal_min_power(g,1,12))