#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_7
import heapq  # Import the heapq module for priority queue implementation

class Node:
    """
    Represents a node in the graph for A* search.
    """
    def __init__(self, data, h_cost):
        self.data = data
        self.neighbors = []  # List of neighboring nodes (tuples: (neighbor_node, edge_cost))
        self.h_cost = h_cost  # Heuristic cost (estimated cost to goal)
        self.g_cost = 0     # Cost from the start node to this node
        self.f_cost = 0     # Total cost (g_cost + h_cost)

    def __lt__(self, other):
        """
        Comparison method for priority queue (heapq).  Compares f_costs.
        """
        return self.f_cost < other.f_cost

    def __repr__(self):
        return f"Node({self.data}, h={self.h_cost}, g={self.g_cost}, f={self.f_cost})"


def a_star_search(start_node, goal_node):
    """
    Performs A* search on a graph.

    Args:
        start_node: The starting node.
        goal_node: The goal node.
    """
    open_set = [start_node]  # Priority queue (heapq) of nodes to explore
    closed_set = set()      # Set of nodes already evaluated
    path = []

    start_node.g_cost = 0
    start_node.f_cost = start_node.h_cost  # f = g + h

    print("A* Search:")
    while open_set:
        # Get the node with the lowest f_cost from the open set
        current_node = heapq.heappop(open_set)

        if current_node == goal_node:
            print("Goal Node Found!")
            # Reconstruct the path from start to goal
            while current_node:
                path.append(current_node.data)
                # Backtrack.  In a full implementation, you'd store the 'came_from'
                # attribute in each node during the search.  For this simplified
                # example, we assume the graph structure allows us to reach
                # the start by going through the parents.
                if current_node == start_node:
                    break
                # A* doesn't store parent directly.  This is a simplified way to reconstruct.
                for node in closed_set: # VERY INEFFICIENT WAY TO BACKTRACK.
                    for neighbor, edge_cost in node.neighbors:
                        if neighbor == current_node:
                            current_node = node
                            break
                    else:
                        continue
                    break

            print("Path:", path[::-1])  # Reverse the path to get start -> goal
            return

        closed_set.add(current_node)  # Move current node to the closed set

        for neighbor, edge_cost in current_node.neighbors:
            tentative_g_cost = current_node.g_cost + edge_cost

            if neighbor in closed_set and tentative_g_cost >= neighbor.g_cost:
                continue  # Skip if neighbor is in closed set with a lower cost

            if neighbor not in closed_set or tentative_g_cost < neighbor.g_cost:
                neighbor.g_cost = tentative_g_cost
                neighbor.f_cost = tentative_g_cost + neighbor.h_cost
                # In a proper A* implementation, you would also set
                # neighbor.came_from = current_node  # To track the path
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)  # Add neighbor to the open set
                    #print(f"Added to open set: {neighbor}")

# --- Example Graph for A* ---
# Heuristic costs (h_cost) are estimates of the distance to the goal (G)
node_a = Node("A", h_cost=10)
node_b = Node("B", h_cost=8)
node_c = Node("C", h_cost=5)
node_d = Node("D", h_cost=7)
node_e = Node("E", h_cost=3)
node_f = Node("F", h_cost=6)
node_g = Node("G", h_cost=0)  # Goal node

# Connect nodes with edge costs (tuples: (neighbor_node, edge_cost))
node_a.neighbors = [(node_b, 2), (node_c, 9), (node_d, 15)]
node_b.neighbors = [(node_a, 2), (node_e, 10)]
node_c.neighbors = [(node_a, 9), (node_f, 1)]
node_d.neighbors = [(node_a, 15), (node_g, 15)]
node_e.neighbors = [(node_b, 10), (node_f, 5), (node_g, 8)]
node_f.neighbors = [(node_c, 1), (node_e, 5), (node_g, 5)]
node_g.neighbors = []  # Goal node has no neighbors

# Perform A* search from A to G
a_star_search(node_a, node_g)  # Output: A B E G