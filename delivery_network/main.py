from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.05.in"

g = graph_from_file(data_path + file_name)
print(g)
print (g.graph)

print(g.get_path_with_power(2, 4, 7))