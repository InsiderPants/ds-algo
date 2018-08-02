"""
Properties of a Binary Tree :
1. Non-linear Data Structure
2. Order of elements is not important
3. Each node has zero child, one child or two children.
4. Operations on Binary Trees:
    a. Traversals             : traversing the tree
    b. Insert(root,data)      : insert element
    c. Search(root,data)      : search element (return true if element if found, else false)
    d. Size(root)             : Size of Tree
    e. Height(root)           : Height of Tree
    f. Deepest_node(root)     : finding and return deepest node of binary tree
    g. Delete(root,data)      : delete given element
    h. max_element(root)      : find and return max element in binary tree
    i. Display(root)          : Display elements of Binary Tree using one of the traversal methods.
    j. Delete_tree(root)      : Delete whole tree
    
5. Applications of Binary Search Trees :
    a. Expression trees are used in compilers.
    b. Huffman coding trees used in data compression.
    c. Binary Search Trees(BST) which supports search,deletion,insertion in O(logn)(average)
    d. Priority Queue
"""

# Importing necessary packages
import queue # Package for implementing queue

# Structure of Binary Trees

class BinaryTree:
    def __init__(self,data):
        self.data = data  # root node
        self.left = None  # left child
        self.right = None # right child
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def insert_left(self,new_node):
        if (self.get_left() == None): # there's no left child
            self.left = BinaryTree(new_node)
        else:                         # there's a left child present
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp
    def insert_right(self,new_node):
        if (self.get_right() == None): # there's no right child
            self.right = BinaryTree(new_node)
        else:                         # there's a right child present
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp

"""
Binary Tree Traversals

1. Depth-First Search (DFS) : Completely traverse one sub-tree before exploring a sibling sub-tree
    a. PreOrder Traversal  
    b. InOrder Traversal
    c. PostOrder Traversal
    - Uses Stack
    
2. Breadth-First Search (BFS) : Completely traverse all nodes at one level before processing to next level
    a. LevelTraversal
    - Uses Queue
    
Example Tree :       1
                  /     \
                2         3
              /   \     /   \
             4     5   6     7
"""

# PreOrder Traversal   : visit root, traverse left subtree, traverse right subtree.
# Prints : 1 2 4 5 3 6 7
def PreOrder_traversal(root,result):
    if not root: # null tree/node
        return
    result.append(root.get_data())               # visit root
    PreOrder_traversal(root.get_left(),result)   # traverse left subtree
    PreOrder_traversal(root.get_right(),result)  # traverse right subtree
    
# InOrder Traversal    : traverse left subtree, visit root, traverse right subtree.
# Prints : 4 2 5 1 6 3 7
def InOrder_traversal(root,result):
    if not root: # null tree/node
        return
    InOrder_traversal(root.get_left(),result)    # traverse left subtree
    result.append(root.get_data())               # visit root
    InOrder_traversal(root.get_right(),result)   # traverse right subtree
    
# PostOrder Traversal  : traverse left subtree, traverse right subtree, visit root.
# Prints : 4 5 2 6 7 3 1
def PostOrder_traversal(root,result):
    if not root: # null tree/node
        return
    PostOrder_traversal(root.get_left(),result)  # traverse left subtree
    PostOrder_traversal(root.get_right(),result) # traverse right subtree
    result.append(root.get_data())               # visit root
    
# LevelOrder Traversal : 
    # a. visit root
    # b. while traversing level "l", keep all elements at level l+1 in queue
    # c. go to next level and visit all nodes at that level
    # d. repeat until all levels are completed
# Prints : 1 2 3 4 5 6 7
def LevelOrder_traversal(root,result):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)                             # step a. visit root (Enqueue)
    node = None
    while not q.empty():                    # step b.
        node = q.get()                      # (Dequeue)
        result.append(node.get_data())
        if node.get_left() is not None:
            q.put(node.get_left())
        if node.get_right() is not None:
            q.put(node.get_right())
"""
Working of Level Order:

from current example,

Iteration 0 (before loop)
Result : 
Queue  : 1

Iteration 1
Result : 1
Queue  : 2 3

Iteration 2
Result : 1 2
Queue  : 3 4 5

Iteration 3
Result : 1 2 3
Queue  : 4 5 6 7

Iteration 4
Result : 1 2 3 4
Queue  : 5 6 7

Iteration 5
Result : 1 2 3 4 5
Queue  : 6 7

Iteration 6
Result : 1 2 3 4 5 6
Queue  : 7

Iteration 7
Result : 1 2 3 4 5 6 7
Queue  : 0

Now queue is empty, loop terminates.
"""

"""
Inserting an element into Binary Tree. We can use level order traversal and 
insert element whereever we find the node whose left or right child is NULL
""" 
def Insert(root,data):
    new_node = BinaryTree(data) # create new node
    if root is None:
        root = new_node
        return root
    q = queue.Queue()
    q.put(root)
    node = None
    while not q.empty():
        node = q.get()
        # Check for duplicate data
        if (data == node.get_data()):
            return root
        # Check if left is NULL to fill in
        if (node.get_left() is not None):
            q.put(node.get_left())
        else:
            node.left = new_node
            return root
        # Check if right is NULL to fill in
        if (node.get_right() is not None):
            q.put(node.get_right())
        else:
            node.right = new_node
            return root

# Find element in binary tree (return true if element if found, else false)
def Search(root,data):
    if not root: # end of leaf/ empty tree
        return False
    if (root.get_data()==data):
        return True
    else:
        found = Search(root.get_left(),data)  # Search in left subtree
        if found is True:
            return found
        else:
            return Search(root.get_right(),data) # Search in right subtree

# return size of Binary Tree
# algo : calculate size of left subtree, right subtree and add 1(current node) and return to its parent
def Size(root):
    if not root:
        return 0
    return Size(root.get_left()) + Size(root.get_right()) + 1

# return height of Binary Tree
# algo : this is similar to PreOrder tree traversal
def Height(root):
    if not root:
        return 0
    return max(Height(root.get_left()) , Height(root.get_right())) + 1

# find and return deepest node in of binary tree
# On same level, it returns the right-most element
def Deepest_node(root):
    if not root:
        return 0
    q = queue.Queue()
    q.put(root)
    node = None
    while not q.empty():
        node = q.get()
        if(node.get_left() is not None):
            q.put(node.get_left())
        if(node.get_right() is not None):
            q.put(node.get_right())
    return node.get_data()

# delete the given element
# algo : starting at root, find node we want to delete, find deepest node in tree.
# Replace deepest node's data with node to be deleted. Then delete deepest node.
def Delete(root,data):
    # Check if data is present or not
    if Search(root,data) is not True:
        print("Element not present in Tree!")
        return
    # starting at root, find node we want to delete and replace it with deepest node
    q = queue.Queue()
    q.put(root)
    node_to_del = None
    while not q.empty():
        node_to_del = q.get()
        if(node_to_del.get_data()==data):
            node_to_del.set_data(Deepest_node(root))
            break
        if(node_to_del.get_left() is not None):
            q.put(node_to_del.get_left())
        if(node_to_del.get_right() is not None):
            q.put(node_to_del.get_right())
    # delete deepest node
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if(node.get_left() is not None):
            q.put(node.get_left())
        if(node.get_right() is not None):
            q.put(node.get_right())
    del node

# Find maximum element in binary tree
# Algo : get max element from left subtree and from right subtree and compare with root. Select the maximum of the  three.
max_ele = float("-infinity")
def max_element(root):
    global max_ele
    if not root: # end of leaf/ empty tree
        return max_ele
    if (root.get_data() > max_ele):
        max_ele = root.get_data()
    max_element(root.get_left())  # Search in left subtree
    max_element(root.get_right()) # Search in right subtree
    return max_ele

# Display elements of Binary Tree using one of the traversal methods.
def Display(root):
    result = []
    print("Enter the option of traversal while printing :")
    print("Enter 1 for PreOrder Traversal")
    print("Enter 2 for InOrder Traversal")
    print("Enter 3 for PostOrder Traversal")
    print("Enter 4 for LevelOrder Traversal")
    option = input()
    if option not in ["1","2","3","4"]:
        print("Enter valid choice from 1,2,3,4")
        return
    if(option=="1"):
        PreOrder_traversal(root,result)
    if(option=="2"):
        InOrder_traversal(root,result)
    if(option=="3"):
        PostOrder_traversal(root,result)
    if(option=="4"):
        LevelOrder_traversal(root,result)
    if not result:
        print("Tree is empty")
        return
    print(result)

# Delete whole Tree
def Delete_tree(root):
    if not root:
        return
    Delete_tree(root.get_left())
    Delete_tree(root.get_right())
    del root