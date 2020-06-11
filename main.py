class Node:    
  def __init__(self,Note):    
    self.Note = Note;
    self.next = None;    
     
class CreateList:
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
  def add(self,NoteString):    
    '''This function will add the new node at the end of the list.'''
    for Note in NoteString:

        newNode = Node(Note);    
        if self.head.Note is None:    
          #If list is empty, both head and tail would point to new node.    
          self.head = newNode;    
          self.tail = newNode;    
          newNode.next = self.head;    
        else:    
          self.tail.next = newNode;    
          self.tail = newNode;    
          self.tail.next = self.head;    
         
  def transpose(self,Note,num):
      '''transposes chords up and down according to the num given'''
      print(num)
      try :
          if num ==0:
              _=2/num
      except ZeroDivisionError:
          print('Number cant be zero')
          return(0)
          
      current = self.head;
      while current.Note != Note:
          current = current.next
          print('reaching to the required note',current.Note)
      print('reached')
      if num>0:
          while num:
              current = current.next
              num-=1
      else :
          num = 12+num
          while num:
              current = current.next
              num-=1
      print(current.Note)


      
class CircularLinkedList:    
  cl = CreateList();    
  #Adds Notes to the list    
  cl.add(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'])
  #Tranpose test
  cl.transpose('F#',7)

  
