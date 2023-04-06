class UnionFind:
    """
    A class representing a Union-Find data structure.
    It is used to implement Kruskal's algorithm to find the minimum spanning tree of a graph.
"""
    def __init__(self, n):
        # Initialize the parent list for each node
        self.parent = list(range(n))
        # Initialize the rank of each node to 0
        self.rank = [0] * n

    def find(self, x):
        # If the node is not its own parent, recursively find its parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        # Set the node's parent to its root node
        return self.parent[x]

    def union(self, x, y):
        # Find the root nodes of the two input nodes
        xroot, yroot = self.find(x), self.find(y)
        # If the nodes are already in the same set, return
        if xroot == yroot:
            return
        # If the rank of the root node of x is less than the rank of the root node of y,
        # make the root node of y the parent of the root node of x
        if self.rank[xroot] < self.rank[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        # If the rank of the root node of x is equal to the rank of the root node of y,
        # increment the rank of the root node of x by 1
        if self.rank[xroot] == self.rank[yroot]:
            self.rank[xroot] += 1





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
        # If the node1 does not exist in the graph, add it to the graph with an empty adjacency list
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        # If the node2 does not exist in the graph, add it to the graph with an empty adjacency list
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        # Add the edge to the adjacency list of both nodes
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    

    def get_path_with_power(self, src, dest, power):
        # Dictionary to store if a node has been visited or not
        nodes_visited = {nodes: False for nodes in self.nodes}
    
        def search_path(nodes, path):
            # If the destination node is reached, return the path
            if nodes == dest:
                 return path
            for neighbour in self.graph[nodes]:     # neighbour sont les voisins cherchés
                neighbour, power_min, dist = neighbour
                nodes_visited[src] = True
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
    


    def kruskal(self):
        # Sort edges by weight
        sort_edges = []
        edges = []

        # Extract all edges from graph
        for i in self.graph:
            for n, p, d in self.graph[i]:
                edges.append((i, n, p, d))
        # Sort edges by weight
        sort_edges = sorted(edges, key=lambda a: a[2])

        # Initialize UnionFind
        uf = UnionFind(self.nb_nodes + max(self.nodes))

        # Create minimum spanning tree
        mst = Graph()
        for node1, node2, weight, d in sort_edges:
            # Check if adding edge creates cycle
            if uf.find(node1) != uf.find(node2):
                # Add edge to minimum spanning tree
                mst.add_edge(node1, node2, weight, d)
                # Merge sets
                uf.union(node1, node2)

        return mst
    

    def oriented_tree(self,root=1): #complexity in O(V+E)
        parent = [k for k in range(self.nb_nodes+1)] 
        rank = [0]*(self.nb_nodes+1)
        power = [0]*(self.nb_nodes+1)

        def DFS(node, father): 
            for child, power_min, dist in self.graph[node]:
                if child!=father: 
                    parent[child]=node  
                    rank[child]=rank[node]+1 
                    power[child]=power_min  
                    DFS(child, node) 

        DFS(1,1) 
        return parent, rank, power 



    def kruskal_min_power(self, dfs, src, dest): # complexité en O(Elog(E))
        parent = dfs[0]
        rank = dfs[1]
        power = dfs[2]
        min_pkr = 0
        traj_src = []
        traj_d = []
        while rank[src] < rank[dest]:
            min_pkr = max(power[dest], min_pkr)
            traj_d += [dest] 
            dest = parent[dest] 
        while rank[dest] < rank[src]:  
            min_pkr = max(power[src], min_pkr)
            traj_src+=[src]
            src=parent[src]
        while dest !=src: 

            min_pkr=max(power[src], power[dest], min_pkr)
            traj_src+=[src]
            traj_d+=[dest]
            src=parent[src]
            dest=parent[dest]
        traj_f=traj_src+[src]+traj_d[::-1]
        return min_pkr, traj_f




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



