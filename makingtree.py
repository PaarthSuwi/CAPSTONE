# making the tree graph 


class Tree:
    def __init__(self): # list jaha pe saare vertices and edges will be considered as a list 
        self.adjacency_list = {}

    def add_node(self, node): # node will be our one point to other point connections 
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2): # edges that are the lines that connect the other points so it represt the line that again is in list 
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

    def print_adjacency_list(self): # for printing the node by which 2 or more points are connected and shows up 
        for node, neighbors in self.adjacency_list.items():
            print(f"{node}: {neighbors}")

# Create a tree
tree = Tree()

# Add nodes
tree.add_node(1)
tree.add_node(2)
tree.add_node(3)
tree.add_node(4)
tree.add_node(5)

# Add edges
tree.add_edge(1, 2)
tree.add_edge(1, 3)
tree.add_edge(2, 4)
tree.add_edge(2, 5)

# Print the adjacency list
tree.print_adjacency_list() # the function created for printing the tree in the form of list h