from graph import Graph, graph_from_file, trucks_from_file, sorted_trucks


data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)



file_name = "trucks.2.in"

print(len(trucks_from_file(data_path + file_name)))
print(len(sorted_trucks(trucks_from_file(data_path + file_name))))
