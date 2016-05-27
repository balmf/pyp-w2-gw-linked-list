import pdb
class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.elem == other.elem and self.next == other.next

    def __repr__(self):
        return "The value of elem: {0}  The value of next: {1}".format(self.elem, self.next)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            
            self.end = Node(elements[-1])
            node = Node(elements[0], None)
            last_node = self.end
            for element in reversed(elements[:-1]):
                node = Node(element, last_node)
                last_node = node
            self.start = node
    

    def __str__(self):
        lst = [str(el) for el in self]
        
        return "[" + ", ".join(lst) + "]"
        
    def __len__(self):
        return self.count()

    def __iter__(self):
        return (node.elem for node in self.iterate_nodes())
        

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
            
        for count, elem in enumerate(self):
            if count == index:
                return elem

            

    def __add__(self, other):
        
        new_list = [el for el in self]
        new_list += [el for el in other]

        return LinkedList(new_list)

    def __iadd__(self, other):
        
        for el in other:
            self.append(el)
            
        return self

    def __eq__(self, other):

        for el1, el2 in zip(self, other):
            if el1 != el2:
                return False
                
        return len(self) == len(other)
                
    def iterate_nodes(self):
        if self.start:
            node = self.start
            while node:
                yield node
                node = node.next
                
    def append(self, elem):
        node = Node(elem)
        if self.end:
            self.end.next = node
        else:
            self.start = node
            
        self.end = node



    def count(self):
        count = 0
        for _ in self:
            count += 1
        return count


    def pop(self, index=None):
    
        if index is None:
            index = len(self) - 1
    
        if self.end is None or index >= len(self):
            raise IndexError()
            
        output = self[index]
        
        if index == 0:
           self.start = self.start.next
        else:
            node_before_pop = self.get_node(index - 1)
            node_to_be_popped = self.get_node(index)
            node_after_pop =  node_to_be_popped.next
            
            node_before_pop.next = node_after_pop 
            
        return output
    
    def get_node(self, index):
        if index < 0:
            index = len(self) + index
            
        for count, node in enumerate(self.iterate_nodes()):
            if count == index:
                return node

        raise IndexError("Out of range")