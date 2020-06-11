#Represents the node of list.    
class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    
     
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
  def add(self,data):    
    '''This function will add the new node at the end of the list.'''
    newNode = Node(data);    
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
      #tail will point to new node.    
      self.tail.next = newNode;    
      #New node will become new tail.    
      self.tail = newNode;    
      #Since, it is circular linked list tail will point to head.    
      self.tail.next = self.head;    
     
  #Displays all the nodes in the list    
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty");    
      return;    
    else:    
        print("Nodes of the circular linked list: ");    
        #Prints each node by incrementing pointer.    
        print(current.data),    
        while(current.next != self.head):    
            current = current.next;    
            print(current.data),    
     
     
class CircularLinkedList:    
  cl = CreateList();    
  #Adds data to the list    
  cl.add(C);    
  cl.add(C#);    
  cl.add(D);    
  cl.add(D#);
  cl.add(E);    
  cl.add(F);    
  cl.add(F#);    
  cl.add(G);    
  cl.add(G#);
  cl.add(A);    
  cl.add(A#);
  cl.add(B);    
  #Displays all the nodes present in the list    
  cl.display();    
