class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({repr(self.data)})'


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) Why and under what conditions?"""
        if self.is_empty:
            size = 0
            node = self.head
            while node is not None:
                size += 1
                node = node.next
            return size
            



    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        self.tail = Node(item)
        node = self.head
        if node is None:
            self.head = Node(item)
        else:
            while node.next != self.tail:
                if node.next is None:
                    node.next = Node(item)
                    break
                else:
                    node = node.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
         

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head

            while node is not None:
                if quality(node.data) == False:
                    node = node.next
                elif node.data is not None:
                    return node.data

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head
        prev_node = None
        while node:
            if node.data == item:
                if prev_node == None:
                    self.head = node.next
                    if node.next == None:
                        self.tail = None
                elif node.next == None:
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    prev_node.next = node.next
                return
            else:
                prev_node = node
                node = node.next
        raise ValueError(f'Item not found: {item}')



def test_linked_list():
    ll = LinkedList()
    print(f'list: {ll}')

    print('\nTesting append:')   
    for item in ['A', 'B', 'C'] :
        print(f'append({repr(item)})')
        ll.append(item)
        print(f'list: {ll}')

    print(f'head: {ll.head}')
    print(f'tail: {ll.tail}')
    print(f'length: {ll.length()}')

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B','C','A',] :
            print(f'delete({repr(item)})')
            ll.delete(item)
            print(f'list: {ll}')

        print(f'head: {ll.head}')
        print(f'tail: {ll.tail}')
        print(f'length: {ll.length()}')

if __name__ == '__main__':
    test_linked_list()

