from graph import Graph, graph_from_file

def trucks_from_file(filename): # Fonction permettant d'ouvrir les fichiers trucks
    L=[]
    with open(filename, "r") as file:
        nb_truck=map(int, file.readline().split())
        nb_truck0=list(nb_truck)[0]
        for _ in range (nb_truck0):
            power,cost=map(int, file.readline().split())
            L.append((power,cost))
    return L


def routes_from_file(filename): # Fonction permettant d'ouvrir les fichiers routes.in  
    L=[]
    with open(filename, "r") as file:
        nb_trajet=map(int, file.readline().split())
        for _ in range (list(nb_trajet)[0]):
            src,dest,profit=map(int, file.readline().split())
            L.append([(src,dest),profit])
    return L



def sorted_trucks1(trucks):
    p_t=trucks[-1][0]
    c_t=trucks[-1][1]
    new_list=[(p_t,c_t)]
    for power, cost in reversed(trucks):
        if power<=p_t and cost<c_t:
            new_list.insert(0,(power,cost))
        c_t=cost
        p_t=power
    return new_list

def sorted_trucks(trucks):
    trucks1 = sorted_trucks1(trucks)
    while trucks1 != sorted_trucks1(trucks1) :
        trucks1 = sorted_trucks1(trucks1)
    return trucks1



"""We need a function that gives us every truck that is link to every routes.
In fact, we know the minimum power for every route and so we just need to check 
the cheapest truck with a power greater or equal to the min_power of the route."""

def truck_for_routes(network, route_file, trucks_file):
    routes = routes_from_file(route_file)
    trucks = sorted_trucks(trucks_from_file(trucks_file))   
    g = graph_from_file(network)
    g_new = g.kruskal()
    h=g_new.oriented_tree()
    min_power = 0
    medium = 0
    min = 0
    max = len(trucks)
    truck_power = int(trucks[medium][0])
    L = []
    for route in routes:
        min_power = int(g.kruskal_min_power(h, route[0][0], route[0][1])[0])
        #print(min_power)    
        medium = int((len(trucks)/2))
        min = 0
        max = len(trucks)
        while max-min > 1:
            truck_power = int(trucks[medium][0])
            if truck_power > min_power:
                max = medium
                medium = int((medium+min)/2)
                min = min
            else:
                min = medium
                medium = int((medium+max)/2)
                max = max
        L.append((route, trucks[min +1]))
    return L


def max_profit(network, route_file, trucks_file):
    truck_routes = truck_for_routes(network, route_file, trucks_file)
    profit = 0
    x = 0
    j = 0
    profit_route = 0
    cost_truck = 0
    power_and_profit=[]
    truck_routes_rapport = []
    for i in range(len(truck_routes)) :
        profit_route = int(truck_routes[i][0][1])
        cost_truck = int(truck_routes[i][1][1])
        rapport = profit_route/cost_truck
        truck_routes_rapport.append(truck_routes[i] + (rapport,))
    truck_routes_rapport.sort(key=lambda truck_routes_rapport : truck_routes_rapport[2], reverse= True)
    while x<25*10**9 and j < len(truck_routes_rapport):
        profit += truck_routes_rapport[j][0][1]
        x += truck_routes_rapport[j][1][1]
        power_and_profit.append(truck_routes_rapport[j][0][0] + (truck_routes_rapport[j][1][0],))
        cost_truck = truck_routes_rapport[j][1][0]
        profit_route = truck_routes_rapport[j][0][1]
        j += 1
    if x > 25*10**9:
        power_and_profit.pop(-1)
        x = x - cost_truck
        profit = profit - profit_route
    power_and_profit = [profit] + power_and_profit
    return power_and_profit, profit, x




