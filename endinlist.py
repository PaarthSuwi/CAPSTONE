class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        
        n1.next = n2
        n2.next = n3
        n3.next = n4
        
        head = n1
        
        new_node = Node(50)
        new_node.next = head
        head = new_node

        def traverse_linked_list(head):
            current = head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("none")
            
        print ("linked list before insertion")
        traverse_linked_list(n1)
        print ("linked list after insertion ")
        traverse_linked_list(head)
        
        