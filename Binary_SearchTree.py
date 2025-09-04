class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
 
    def _insert_recursive(self, current_node, value):
        if value == current_node.value:
            return  # no duplicates allowed
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
 
    def search(self, value):
        return self._search_recursive(self.root, value)
 
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
 
    def inorder(self):
        return self._inorder_recursive(self.root)
 
    def _inorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.value)
            result.extend(self._inorder_recursive(node.right))
        return result
 
    def preorder(self):
        return self._preorder_recursive(self.root)
 
    def _preorder_recursive(self, node):
        result = []
        if node:
            result.append(node.value)
            result.extend(self._preorder_recursive(node.left))
            result.extend(self._preorder_recursive(node.right))
        return result
 
    def postorder(self):
        return self._postorder_recursive(self.root)
 
    def _postorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._postorder_recursive(node.left))
            result.extend(self._postorder_recursive(node.right))
            result.append(node.value)
        return result
 
bst = BinarySearchTree()
elements = [28, 36, 15, 5, 3, 34, 20]
for el in elements:
    bst.insert(el)
print("Search 5:", bst.search(5))   
print("Search 8:", bst.search(8))  
 
print("Inorder traversal:", bst.inorder())     
print("Preorder traversal:", bst.preorder())   
print("Postorder traversal:", bst.postorder()) 
 
 