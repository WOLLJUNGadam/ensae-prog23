from graph import Graph, graph_from_file
from optimisation import trucks_from_file, sorted_trucks, routes_from_file, truck_for_routes, max_profit


data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)



file_name = "trucks.1.in"

print(len(trucks_from_file(data_path + file_name)))
print(len(sorted_trucks(trucks_from_file(data_path + file_name))))

"""print(truck_for_routes(data_path + "network.2.in", data_path + "routes.2.in", data_path + "trucks.2.in"))


opti1 = truck_for_routes(data_path + "network.2.in", data_path + "routes.2.in", data_path + "trucks.2.in")

routes = routes_from_file(data_path + "routes.2.in")
g = graph_from_file(data_path +"network.2.in")
g_new = g.kruskal()
h=g_new.oriented_tree()

for i in range(100):
    print(int(g.kruskal_min_power(h, routes[i][0][0], routes[i][0][1])[0]))
    print(opti1[i])
"""
#print(sorted_trucks(trucks_from_file(data_path + "trucks.2.in")))

a,b,c = max_profit(data_path + "network.3.in", data_path + "routes.3.in", data_path + "trucks.2.in")
print(a)
print(b)
print(c)

#print(type(truck_for_routes(data_path + "network.2.in", data_path + "routes.2.in", data_path + "trucks.2.in")[0][0][1]))

#print(truck_for_routes(data_path + "network.2.in", data_path + "routes.2.in", data_path + "trucks.2.in")[0][1][1])