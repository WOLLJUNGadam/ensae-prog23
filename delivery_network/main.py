from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)

g = graph_from_file(data_path + file_name)
g_new = g.kruskal()
h=g_new.oriented_tree()

print(g.kruskal_min_power(h,1,4))
