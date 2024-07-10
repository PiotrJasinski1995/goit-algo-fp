class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def reverse_list(self):
        if self.head is None:
            return
        else:
            reverse_l = LinkedList()
            cur = self.head
            reverse_l.head = Node(self.head.data) if self.head else None

            while cur.next:   
                new_node = Node(cur.next.data)
                new_node.next = reverse_l.head
                reverse_l.head = new_node
                cur = cur.next
            
            self.head = reverse_l.head
    
    @staticmethod
    def getMiddle(head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
                fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    @staticmethod
    def __sortMerge(h):
        if h == None or h.next == None:
            return h

        middle = LinkedList.getMiddle(h)
        nexttomiddle = middle.next

        middle.next = None

        left = LinkedList.__sortMerge(h)
        right = LinkedList.__sortMerge(nexttomiddle)

        sortedlist = LinkedList.sortedMerge(left, right)
        return sortedlist
    
    def mergeSort(self, head):
        self.head = LinkedList.__sortMerge(head)
    
    @staticmethod
    def sortedMerge(a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        if a.data <= b.data:
            result = a
            result.next = LinkedList.sortedMerge(a.next, b)
        else:
            result = b
            result.next = LinkedList.sortedMerge(a, b.next)
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def sort_merge_two_lists(list_1, list_2):
    if list_1.head is None:
            merged_list = list_2
    elif list_2.head is None:
        merged_list = list_1
    else:
        cur = list_1.head
        while cur.next:
            cur = cur.next
        cur.next = list_2.head
        merged_list = list_1

    merged_list.mergeSort(merged_list.head)

    return merged_list


llist = LinkedList()

# Insert the nodes into the end
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Insert the nodes into the end
llist.insert_at_end(20)
llist.insert_at_end(25)

# Printing a linked list
print("Linked list:")
llist.print_list()

# Delete a node
llist.delete_node(10)

print("\nThe linked list after deleting the node with data 10:")
llist.print_list()

# Searching for an item in a linked list
print("\nSearching for element 15:")
element = llist.search_element(15)
if element:
    print(element.data)

print("\nThe linked list after reversal:")
llist.reverse_list()
llist.print_list()

print("\nThe linked list after merge sorting:")
llist.mergeSort(llist.head)
llist.print_list()

lllist = LinkedList()
# Insert the nodes into the end
lllist.insert_at_beginning(31)
lllist.insert_at_beginning(32)
lllist.insert_at_beginning(33)
lllist.insert_at_beginning(34)
lllist.insert_at_beginning(35)
lllist.insert_at_beginning(36)

print("\nNew linked list:")
lllist.print_list()

merged_list = sort_merge_two_lists(llist, lllist)
print("\nMerged list:")
merged_list.print_list()
