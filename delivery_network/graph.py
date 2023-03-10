class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    

    def get_path_with_power(self, src, dest, power):
        nodes_visited = {nodes: False for nodes in self.nodes}
    
        def search_path(nodes, path):
            if nodes == dest:
                 return path
            for neighbour in self.graph[nodes]:     # neighbour sont les voisins cherchés
                neighbour, power_min, dist = neighbour
                if not nodes_visited[neighbour] and power_min  <= power :
                    nodes_visited[neighbour] = True 
                    result =  search_path(neighbour, path + [neighbour])
                    if result is not None:
                        return result
            return None

        return search_path(src, [src])

    def connected_components(self):
        '''retourne une liste de listes (une par composante connectée)''' #FICHIER À CHANGER, LES COMPOSANTES CONNECTÉES SONT LES POINTS QUI SONT CONNECTÉS AU SENS OÙ IL EXISTE UN CHEMIN POUR REJOINDRE TOUS CES POINTS
        list_components = []
        nodes_visited = {nodes: False for nodes in self.nodes}
    
        def dfs(nodes):
            component = [nodes]
            for i in self.graph[nodes]:
                i = i[0]
                if not nodes_visited[i]:      # i étant les voisins cherchés  
                      nodes_visited[i] = True
                      component = component + dfs(i)
            return component
        
        for i in self.nodes:
            if not nodes_visited[i]:
                list_components.append(dfs(i))

        return list_components
    
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """      
        list_power = []
        for i in self.nodes:
            for k in self.graph[i]:
                list_power.append(k[1])
        list_power = sorted(list(set(list_power)))
        power = list_power[int((len(list_power)/2))]
        medium = int((len(list_power)/2))
        min = 0
        max = len(list_power)
        result = self.get_path_with_power(src, dest, list_power[min])
        if result is not None:
            return result, list_power[min]
        result = self.get_path_with_power(src, dest, power)
        while max-min > 1:
            if result is not None:
                max = medium
                medium = int((medium+min)/2)
                min = min
                power = list_power[medium]
                result = self.get_path_with_power(src, dest, power)
            elif result is None:
                min = medium
                medium = int((medium+max)/2)
                max = max
                power = list_power[medium]
                result = self.get_path_with_power(src, dest, power)
        return self.get_path_with_power(src, dest, list_power[max]), list_power[max]




def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g
