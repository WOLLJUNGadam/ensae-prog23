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



def sorted_trucks(trucks):
    p_t=trucks[-1][0]
    c_t=trucks[-1][1]
    new_list=[(p_t,c_t)]
    for power, cost in reversed(trucks):
        if power<=p_t and cost<c_t:
            new_list.insert(0,(power,cost))
        c_t=cost
        p_t=power
    return new_list
