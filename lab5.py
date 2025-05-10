#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_5
class Node:
    """
    Represents a node in the graph.
    """
    def __init__(self, data):
        self.data = data
        self.neighbors = []  # List of neighboring nodes

    def __repr__(self):
        return f"Node({self.data})"

def dfs_with_stack(start_node):
    """
    Performs Depth-First Search (DFS) on a graph using a stack.

    Args:
        start_node: The starting node for the DFS traversal.
    """
    stack = [start_node]  # Initialize the stack with the starting node
    visited = set()      # Set to keep track of visited nodes
    path = []

    print("DFS Traversal (with stack):")
    while stack:
        node = stack.pop()  # Pop the top node from the stack
        if node not in visited:
            visited.add(node)    # Mark the node as visited
            path.append(node.data)
            print(node, end=" ")  # Process the node (e.g., print its data)

            # Add neighbors to the stack
            for neighbor in reversed(node.neighbors): # Important: Reverse to maintain DFS order
                if neighbor not in visited:
                    stack.append(neighbor)
    print("\nPath:", path)


# Create nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

# Connect nodes to form a graph
node_a.neighbors = [node_b, node_c]
node_b.neighbors = [node_d, node_e]
node_c.neighbors = [node_f]
node_d.neighbors = [node_e]
node_e.neighbors = [node_f]

# Perform DFS starting from node A
dfs_with_stack(node_a)  
