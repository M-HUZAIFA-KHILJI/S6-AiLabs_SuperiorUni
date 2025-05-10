#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_6 
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, data):
        self.data = data
        self.left = None   # Left child
        self.right = None  # Right child

    def __repr__(self):
        return f"TreeNode({self.data})"

def preorder_dfs(node):
    """
    Performs Preorder DFS traversal of a binary tree.
    (Root, Left, Right)
    """
    if node:
        print(node.data, end=" ")  # Process (print) the root node *first*
        preorder_dfs(node.left)     # Recursively traverse the left subtree
        preorder_dfs(node.right)    # Recursively traverse the right subtree

def inorder_dfs(node):
    """
    Performs Inorder DFS traversal of a binary tree.
    (Left, Root, Right)
    """
    if node:
        inorder_dfs(node.left)      # Recursively traverse the left subtree *first*
        print(node.data, end=" ")  # Process (print) the root node
        inorder_dfs(node.right)     # Recursively traverse the right subtree

def postorder_dfs(node):
    """
    Performs Postorder DFS traversal of a binary tree.
    (Left, Right, Root)
    """
    if node:
        postorder_dfs(node.left)     # Recursively traverse the left subtree *first*
        postorder_dfs(node.right)    # Recursively traverse the right subtree
        print(node.data, end=" ")  # Process (print) the root node *last*

# --- Example Binary Tree ---
# Create nodes
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")
node_f = TreeNode("F")
node_g = TreeNode("G")

# Connect nodes to form a binary tree
root.left = node_b
root.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

print("\n\n--- Binary Tree Traversal (DFS Orders) ---")
print("Preorder DFS:")
preorder_dfs(root)  # Output: A B D E C F G

print("\nInorder DFS:")
inorder_dfs(root)    # Output: D B E A F C G

print("\nPostorder DFS:")
postorder_dfs(root)  # Output: D E B F G C A