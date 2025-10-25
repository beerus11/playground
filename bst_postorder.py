from tree_node import Node

class BSTPostOrder:
    def __init__(self, node):
        self.node = node
        self.st = [self.node] if self.node else []
        self.visited = set()

    def has_next(self):
        if not self.st:
            return False
        return True

    def next(self):
        if not self.has_next():
            raise Exception("No element found")
        
        while self.st:
            node = self.st[-1]
            if node in self.visited:
                self.st.pop()
                return node.value
            self.visited.add(node)
            if node.right:
                self.st.append(node.right)
            if node.left:
                self.st.append(node.left)
        
        raise Exception("No element found")


# Test cases
if __name__ == "__main__":
    # Test 1: Simple tree
    print("Test 1: Simple tree")
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    
    bst = BSTPostOrder(root)
    result = []
    while bst.has_next():
        result.append(bst.next())
    print(f"Postorder: {result}")  # Expected: [1, 3, 2, 5, 7, 6, 4]
    
    # Test 2: Single node
    print("\nTest 2: Single node")
    single = Node(10)
    bst2 = BSTPostOrder(single)
    result2 = []
    while bst2.has_next():
        result2.append(bst2.next())
    print(f"Postorder: {result2}")  # Expected: [10]
    
    # Test 3: Left skewed tree
    print("\nTest 3: Left skewed tree")
    left_skewed = Node(4)
    left_skewed.left = Node(3)
    left_skewed.left.left = Node(2)
    left_skewed.left.left.left = Node(1)
    
    bst3 = BSTPostOrder(left_skewed)
    result3 = []
    while bst3.has_next():
        result3.append(bst3.next())
    print(f"Postorder: {result3}")  # Expected: [1, 2, 3, 4]
    
    # Test 4: Right skewed tree
    print("\nTest 4: Right skewed tree")
    right_skewed = Node(1)
    right_skewed.right = Node(2)
    right_skewed.right.right = Node(3)
    right_skewed.right.right.right = Node(4)
    
    bst4 = BSTPostOrder(right_skewed)
    result4 = []
    while bst4.has_next():
        result4.append(bst4.next())
    print(f"Postorder: {result4}")  # Expected: [4, 3, 2, 1]
    
    # Test 5: Empty tree (None root)
    print("\nTest 5: Empty tree")
    bst5 = BSTPostOrder(None)
    result5 = []
    while bst5.has_next():
        result5.append(bst5.next())
    print(f"Postorder: {result5}")  # Expected: []
    
    # Test 6: has_next() and next() edge cases
    print("\nTest 6: Edge cases")
    empty_bst = BSTPostOrder(Node(1))
    empty_bst.next()  # Remove the only element
    print(f"has_next() after removing all: {empty_bst.has_next()}")  # Expected: False
    
    try:
        empty_bst.next()  # Should raise exception
    except Exception as e:
        print(f"Exception when calling next() on empty: {e}")
    
    # Test 7: Complex tree
    print("\nTest 7: Complex tree")
    complex_root = Node(1)
    complex_root.left = Node(2)
    complex_root.right = Node(3)
    complex_root.left.left = Node(4)
    complex_root.left.right = Node(5)
    complex_root.right.left = Node(6)
    complex_root.right.right = Node(7)
    
    bst7 = BSTPostOrder(complex_root)
    result7 = []
    while bst7.has_next():
        result7.append(bst7.next())
    print(f"Postorder: {result7}")  # Expected: [4, 5, 2, 6, 7, 3, 1]
