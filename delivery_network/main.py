from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.04.in."

g = graph_from_file(data_path + file_name)
print(g)
print (g.graph)

print(g.connected_components_set())

print(g.graph) 

g.get_path_with_power(1, 3, 5)