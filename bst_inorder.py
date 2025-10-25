from tree_node import Node

class BSTInOrder:
    def __init__(self,node):
        self.node = node
        self.st = [self.node]
        self.move_to_left(self.node)

    def move_to_left(self,node):
        if not node:
            return
        while node.left:
            self.st.append(node.left)
            node = node.left


    def has_next(self):
        if not self.st:
            return False
        return True

    def next(self):
        if not self.has_next():
            raise Exception("No element found")

        node = self.st.pop()
        if node.right :
            self.st.append(node.right)
            self.move_to_left(node.right)
        return node.value


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
    
    bst = BSTInOrder(root)
    result = []
    while bst.has_next():
        result.append(bst.next())
    print(f"Inorder: {result}")
    
    # Test 2: Single node
    print("\nTest 2: Single node")
    single = Node(10)
    bst2 = BSTInOrder(single)
    result2 = []
    while bst2.has_next():
        result2.append(bst2.next())
    print(f"Inorder: {result2}")
    
    # Test 3: Left skewed tree
    print("\nTest 3: Left skewed tree")
    left_skewed = Node(4)
    left_skewed.left = Node(3)
    left_skewed.left.left = Node(2)
    left_skewed.left.left.left = Node(1)
    
    bst3 = BSTInOrder(left_skewed)
    result3 = []
    while bst3.has_next():
        result3.append(bst3.next())
    print(f"Inorder: {result3}")
    
    # Test 4: Right skewed tree
    print("\nTest 4: Right skewed tree")
    right_skewed = Node(1)
    right_skewed.right = Node(2)
    right_skewed.right.right = Node(3)
    right_skewed.right.right.right = Node(4)
    
    bst4 = BSTInOrder(right_skewed)
    result4 = []
    while bst4.has_next():
        result4.append(bst4.next())
    print(f"Inorder: {result4}")
    
    # Test 5: Empty tree (None root)
    print("\nTest 5: Empty tree")
    try:
        bst5 = BSTInOrder(None)
        result5 = []
        while bst5.has_next():
            result5.append(bst5.next())
        print(f"Inorder: {result5}")
    except:
        print("Error with empty tree")
    
    # Test 6: has_next() and next() edge cases
    print("\nTest 6: Edge cases")
    empty_bst = BSTInOrder(Node(1))
    empty_bst.next()  # Remove the only element
    print(f"has_next() after removing all: {empty_bst.has_next()}")
    
    try:
        empty_bst.next()  # Should raise exception
    except Exception as e:
        print(f"Exception when calling next() on empty: {e}")

        