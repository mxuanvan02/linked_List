class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # chèn vào đầu llist
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  # chèn vào sau 1 node
  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  # chèn vào cuối llist
  def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
      last.next = new_node
      break

  # xoá node
  def deleteNode(self, key):
    temp = self.head
    # xoá phần tử head
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        return
    # Tìm node cần xoá
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    if temp == None:
      return
    # Cô lập Node
    prev.next = temp.next
    temp = None

  # tìm kiếm node
  def search(self, x): 
    current = self.head 
    while current != None: 
      if current.data == x:
        return True
      current = current.next
    return False

  # in llist
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next





