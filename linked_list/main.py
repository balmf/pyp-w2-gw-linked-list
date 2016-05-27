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
        repr(self.elem)


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

        if not self.start:
            return "[]"
        lst = [str(el) for el in self]
        
        return "[" + ", ".join(lst) + "]"
        
    def __len__(self):
        return self.count()

    def __iter__(self):
        if self.start:
            node = self.start
            while node:
                yield node.elem
                if not node.next:
                    break
                node = node.next
        
            

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        count = 0
        for elem in self:
            if count == index:
                return elem
            count += 1
            

    def __add__(self, other):
        
        new_list = [el for el in self]
        new_list += [el for el in other]
        
            
        return LinkedList(new_list)

    def __iadd__(self, other):
        
        for el in other:
            self.append(el)
            
        return self

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if not len(self) == len(other):
            return False
            
        for el1, el2 in zip(self, other):
            if el1 != el2:
                return False
        return True
                

    def append(self, elem):
        node = Node(elem)
        if self.end:
            self.end.next = node
        else:
            self.start = node
            
        self.end = node



    def count(self):
        count = 0
        for el in self:
            count += 1
        return count

    def pop(self, index=None):
    
        if self.end == None:
            raise IndexError()
        
        if index is None:
            index = len(self) - 1
            
        output = self[index]
        
        if index == 0:
            if len(self) == 1:
                self.start = None
                self.end = None
            try:
                self.start = self.get_node(1)
            except:
                self.start = None
                
        else:
            node_before_pop = self.get_node(index - 1)
            node_to_pop = self.get_node(index)
            
            try:
                node_after_pop = self.get_node(index+1)
            except:
                node_after_pop = None
            
            node_before_pop.next = node_after_pop 
            
            
            self.start = self.get_node(0)
            self.end = self.get_node(-1)

        return output
    
    def get_node(self, index):
        if index < 0:
            index = len(self) + index
        node = self.start
        count = 0
        while node.next:
            if count == index:
                return node
            count += 1
            node = node.next
            
        if count < index:
            raise IndexError("Out of range")
        return node