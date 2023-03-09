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
            for i in self.graph[nodes]:     # i étant les voisins cherchés
                i, power_min, dest = i
                if not nodes_visited[i] and power_min  <= power :
                    nodes_visited[i] = True 
                    result =  search_path(i, path + [i])
                    if result is not None:
                        return result
            return None
        
        return search_path(src, [src ])
    

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
        '''
        test = False
        output = [[]]
        l = int(0)
        tailleoutput = len(output)
        for i in range(1,self.nb_nodes):
            tailleoutput = len(output)
            for j in range(1,tailleoutput):
                if i in output[j]:
                    test = True
                    l = j
                print(test)
                if test : 
                    output(l).append([i])
                else : 
                    output.append([i])
                print(output)
        '''
        '''
        output = [[1]]
        for i in range(1,self.nb_nodes):
            t = len(output)
            for k in range(t):
                if i in output[k]:
                    for j in range(len(self.graph[i]) - 1):
                        if j not in output[k]:
                            output[k].append(j)
        return output'''
        '''python delivery_network/main.py
            The graph has 7 nodes and 5 edges.
            1-->[(2, 1, 1)]
            2-->[(1, 1, 1), (3, 1, 1)]
            3-->[(2, 1, 1)]
            4-->[(5, 1, 1)]
            5-->[(4, 1, 1), (7, 1, 1)]
            6-->[(7, 1, 1)]
            7-->[(6, 1, 1), (5, 1, 1)]
            [1, 2], [2, 3], [4, 5]]
            (base) adamwolljung@MacBook-Air-de-Adam ensae-prog23 % '''


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
        raise NotImplementedError


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
