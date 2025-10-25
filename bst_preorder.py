
from tree_node import Node

class BSTPreorder:
    def __init__(self, node):
        self.node = node
        self.st = [self.node]

    def has_next(self):
        if len(self.st)==0:
            return False
        return True

    def next(self):
        if not self.has_next():
            raise Exception("No element found")
        node = self.st.pop()
        if node.right:
            self.st.append(node.right)
        if node.left:
            self.st.append(node.left)
        return node.value


# Test cases
if __name__ == "__main__":
    # Test 1: Simple tree
    print("Test 1: Simple tree")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    bst = BSTPreorder(root)
    result = []
    while bst.has_next():
        result.append(bst.next())
    print(f"Preorder: {result}")
    
    # Test 2: Single node
    print("\nTest 2: Single node")
    single = Node(10)
    bst2 = BSTPreorder(single)
    result2 = []
    while bst2.has_next():
        result2.append(bst2.next())
    print(f"Preorder: {result2}")  # Expected: [10]
    
    # Test 3: Left skewed tree
    print("\nTest 3: Left skewed tree")
    left_skewed = Node(1)
    left_skewed.left = Node(2)
    left_skewed.left.left = Node(3)
    left_skewed.left.left.left = Node(4)
    
    bst3 = BSTPreorder(left_skewed)
    result3 = []
    while bst3.has_next():
        result3.append(bst3.next())
    print(f"Preorder: {result3}")  # Expected: [1, 2, 3, 4]
    
    # Test 4: Right skewed tree
    print("\nTest 4: Right skewed tree")
    right_skewed = Node(1)
    right_skewed.right = Node(2)
    right_skewed.right.right = Node(3)
    right_skewed.right.right.right = Node(4)
    
    bst4 = BSTPreorder(right_skewed)
    result4 = []
    while bst4.has_next():
        result4.append(bst4.next())
    print(f"Preorder: {result4}")  # Expected: [1, 2, 3, 4]
    
    # Test 5: Empty tree (None root)
    print("\nTest 5: Empty tree")
    try:
        bst5 = BSTPreorder(None)
        print("Empty tree handled")
    except:
        print("Error with empty tree")
    
    # Test 6: has_next() and next() edge cases
    print("\nTest 6: Edge cases")
    empty_bst = BSTPreorder(Node(1))
    empty_bst.next()  # Remove the only element
    print(f"has_next() after removing all: {empty_bst.has_next()}")  # Expected: False
    
    try:
        empty_bst.next()  # Should raise exception
    except Exception as e:
        print(f"Exception when calling next() on empty: {e}")