class LinkedList :

    def __init__(self):
        """
        Initialises a new linked list object.
        @pre:  -
        @post: A new empty linked list object has been initialised.
               It has 0 length, contains no nodes and the head points to None.
        """
        self.__length = 0
        self.__head = None

    def size(self):
        """
        Returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def first(self):
        return self.__head

    def add(self, date):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre: self is a (possibly empty) LinkedList
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        node = Node(date,self.__head)
        self.__head = node
        self.__length += 1

    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")

#Node class

class Node:

    def __init__(self,date=None,cargo=None, next=None):
        """
        Initialises a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, a node with empty cargo (None) and no reference (None) is created.
        """
        self.__dt = date
        self.__cargo = cargo
        self.__next  = next

    def value(self):
        """
        Returns the value of the cargo contained in this node.
        @pre:  -
        @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

        """
        return self.__dt
    def todo(self):
        """Returns the schedule of the day"""
        return self.__cargo

    def next(self):
        return self.__next.value()

    def __str__(self):
        """
        Returns a string representation of the cargo of this node.
        @pre:  self is possibly empty Node object.
        @post: returns a print representation of the cargo contained in this Node.
        """
        return str(self.todo())

    def print_list(self):
        """
        Prints the cargo of this node and then recursively of each node connected to this one.
        @pre:  self is a node (possibly connected to a next node).
        @post: Has printed a space-separated list of the form "a b c ... ",
               where "a" is the string-representation of this node,
               "b" is the string-representation of my next node, and so on.
               A space is printed after each printed value.
        """
        print(self, end="")   # print my head
        tail = self.__next    # go to my next node
        if tail is not None : # as long as the end of the list has not been reached
            tail.print_list() # recursively print remainder of the list

    def print_backward(self):
        """
        Recursively prints the cargo of each node connected to this node (in opposite order),
        and then prints the cargo of this node as last value.
        @pre:  self is a node (possibly connected to a next node).
        @post: Has printed a space-separated list of the form "... c b a",
               where a is my cargo (self), b is the cargo of the next node, and so on.
               The nodes are printed in opposite order: the last nodes' value is printed first.
        """
        tail = self.__next        # go to my next node
        if tail is not None :     # as long as the end of the list has not been reached
            tail.print_backward() # recursively print remainder of the list backwards
        print(head, end = " ")    # print my head



wednesday=Node(22,"LLN")
tuesday=Node(21,"Shopping",next=wednesday)
monday=Node(20,"revision",next=tuesday)
print(monday.value())
print(monday.next())