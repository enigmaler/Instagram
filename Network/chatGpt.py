class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def display_data(self):
        print("ListNode Data:", self.data)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def display_data(self):
        print("TreeNode Data:", self.data)

    def get_list_node_data(self):
        # Assuming there's a ListNode associated with this TreeNode
        if hasattr(self, 'list_node') and isinstance(self.list_node, ListNode):
            return self.list_node.data
        else:
            return None

# Example of establishing a relationship between TreeNode and ListNode
tree_node = TreeNode(10)
list_node = ListNode(45)
tree_node.list_node = list_node  # Associate a ListNode with the TreeNode

# Accessing methods of ListNode from TreeNode
tree_node.list_node.display_data()  # Output: ListNode Data: 5
print("Data of ListNode associated with TreeNode:", tree_node.get_list_node_data())  # Output: Data of ListNode associated with TreeNode: 5
