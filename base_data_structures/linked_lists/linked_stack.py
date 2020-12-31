from base_data_structures.myexception import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    # --------------------- Node class -----------------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # -----------------------Stack methods-------------------------------------------

    def __init__(self):
        """Create an empty stack """
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack """
        node = self._Node(e, None)
        node._next = self.head
        self.head = node
        self._size += 1

    def top(self):
        """Return the element of the top node, but don't remove"""
        if self.is_empty():
            raise Empty("Link stack is empty!")
        else:
            return self.head._element

    def pop(self):
        """Return the element of the top node, and remove the node"""
        if self.is_empty():
            raise Empty("Link stack is empty!")
        else:
            element = self.head._element
            self.head = self.head._next
            self._size -= 1
            return element


    def __str__(self):
        link_str = ""
        cur = self.head
        link_str += f"length: {self._size} || "

        if not self.head:  # empty link stack and head is None
            link_str += "(head|None)"
        else:
            while cur:
                if cur == self.head:
                    link_str += f"(head|{cur._element})->"
                else:
                    link_str += f"({cur._element})->"

                cur = cur._next
            link_str += "None"

        return link_str




if __name__ == '__main__':
    link_stack = LinkedStack()
    link_stack.push('1')
    link_stack.push('2')
    link_stack.push('3')
    print(link_stack)  # 3 || (head|3)->(2)->(1)->None

    link_stack = LinkedStack()
    print(link_stack)  # length: 0 || (head|None)

    link_stack = LinkedStack()
    link_stack.push('1')
    print(link_stack)  # length: 1 || (head|1)->None
    link_stack.pop()
    print(link_stack)  # length: 0 || (head|None)

    link_stack.pop()
    print(link_stack)  # Get assert exception




