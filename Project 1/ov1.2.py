# Jennifer Ly, grudat20 uppg 1.2

# A list element that stores a value of type T
class ListElement:
    def __init__(self, data): 
        """Constructs elements (nodes)"""   
        self.data = data
        self.next = None         

# A singly linked list of elements of type T.
class LinkedList:
    def __init__(self): 
        """Constructs an empty list"""
        self.__first = None      # first element in list
        self.__last = None       # last element in list
        self.__size = 0          # number of elements in list

    # Insert the given element at the beginning of this list.
    # O(1)
    def addFirst(self, element):
        newElement = ListElement(element)      # creates a new element 
        newElement.next = self.__first         # new element points to first element 
        self.__first = newElement              # first element is new element
        self.__size += 1                       
        if self.__last == None:                # the only element
            self.__last = self.__first 
        
    # Insert the given element at the end of this list.
    # O(1)
    def addLast(self, element):
        newElement = ListElement(element)  
        if self.__last != None:
            self.__last.next = newElement      # last element points to new element
            self.__last = self.__last.next     # last element is new element 
            self.__size += 1
        else:
            self.__last = self.__first = newElement

    # Return the first element of this list.
    # Return null if the list is empty.
    # O(1)
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__first.data

    # Return the last element of this list.
    # Return null if the list is empty.
    # O(1)
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__last.data

    # Return the element at the specified position in this list.
    # Return null if index is out of bounds.
    # O(n)
    def get(self, i):
        if i < 0 or i > self.__size-1: 
            return None
        else:
            current = self.__first
            for j in range(0, i):
                current = current.next
            return current.data
               
    # Remove and returns the first element from this list.
    # Return null if the list is empty.
    # O(1)
    def removeFirst(self):
        if self.__size == 0:
            return None 
        else:
            temp = self.__first                 # keep first element temporarily
            self.__first = self.__first.next    # the next element will be the first
            self.__size -= 1
            if self.__size == 0:                # list becomes empty
                self.__last = None
        return temp.data                        # returns deleted element

    # Remove all elements from this list.
    # O(n)
    def clear(self):
        for j in range(0, self.__size):
            self.__first = self.__first.next
            self.__size -= 1
        self.__last = None
        
    # Return the number of elements in this list.
    # O(1)
    def size(self):
        return self.__size     

    # Return a string representation of this list.
    # O(n)
    def string(self):
        linkedList = "["
        current = self.__first
        for j in range(0, self.__size):
            linkedList += str(current.data)
            current = current.next
            if current != None:
                linkedList += ", "
        linkedList += "]"
        return linkedList
    
    # Tests if linked list is correct
    # O(n)
    def healthy(self):
        if self.__size == 0:
            if self.__first == self.__last == None:
                return True
        else:
            current = self.__first
            c = 1
            for j in range(0, self.__size-1):
                current = current.next
                c += 1 
            if self.__size == c and self.__last.next == None:
                return True
            
# Unit test 
def main():
    l = LinkedList() # creates empty list

    # Tests the size when list is empty
    assert l.size() == 0
    assert l.string() == "[]" 
    assert l.getFirst() == None
    assert l.getLast() == None
    assert l.healthy()

    # Tests list after elements been added 
    l.addFirst(0)
    l.addFirst(-1)
    l.addFirst(-2)
    l.addLast(1)
    l.addLast(2)
    assert l.size() == 5
    assert l.string() == "[-2, -1, 0, 1, 2]"
    assert l.healthy()

    # Tests the get functions (get first, last and specified element)
    first = l.getFirst()
    last = l.getLast()
    spec = l.get(2)
    res = [first, spec, last]
    exp = [-2, 0, 2] 
    assert res == exp
    assert l.healthy()

    # Tests if the removed element is in fact the first element
    assert l.removeFirst() == -2
    assert l.size() == 4
    assert l.string()  == "[-1, 0, 1, 2]"
    assert l.healthy()

    # Tests empty list 
    l.clear()
    assert l.size() == 0
    assert l.string() == "[]" 
    assert l.getFirst() == None
    assert l.getLast() == None
    assert l.healthy() 


main()



