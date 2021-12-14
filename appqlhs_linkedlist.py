from tkinter import * 
from tkinter import ttk

root = Tk()
root.title('Quản lí học sinh')
root.geometry("1200x600")

# Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# LinkedList

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def deleteNode(self, key):
    temp = self.head
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        return
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    if temp == None:
      return
    prev.next = temp.next
    temp = None

  def insertList(self):
    global count
    temp = self.head
    while temp:
      if count % 2 == 0:  
        my_tree.insert(parent="", index="end", iid=count, text='', values=(temp.data[0], temp.data[1], temp.data[2], temp.data[3], temp.data[4], temp.data[5], temp.data[6], temp.data[7]), tags="evenrow")
      else:
        my_tree.insert(parent="", index="end", iid=count, text='', values=(temp.data[0], temp.data[1], temp.data[2], temp.data[3], temp.data[4], temp.data[5], temp.data[6], temp.data[7]), tags="oddrow")
      count += 1
      temp = temp.next


# List
llist = LinkedList()

# Count
count = 0



# Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
my_tree.pack()

# Configure the scrollbar
tree_scroll.config(command=my_tree.yview)


# Add some style
style = ttk.Style()


# Pick a theme
style.theme_use("default")


# Configure out treeview colors
style.configure("Treeview",
  background='white',
  foreground='black',
  rowheight=20,
  fieldbackground='white',
  )

# Changed selected color
style.map("Treeview", background=[('selected', '#7f91eb')])

# Define columns
my_tree['columns'] = ("Name", "Class", "Date", "Hometown", "Dadname", "Momname", "Phonenum", "Sponsor")

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="#93c0ed")

# Format column
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=150)
my_tree.column("Class", anchor=CENTER, width=100)
my_tree.column("Date", anchor=CENTER, width=100)
my_tree.column("Hometown", anchor=CENTER, width=150)
my_tree.column("Dadname", anchor=W, width=150)
my_tree.column("Momname", anchor=W, width=150)
my_tree.column("Phonenum", anchor=CENTER, width=100)
my_tree.column("Sponsor", anchor=W, width=150)

# Create Headings
my_tree.heading("#0", text="Label", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Class", text="Class", anchor=CENTER)
my_tree.heading("Date", text="Date", anchor=CENTER)
my_tree.heading("Hometown", text="Home Town", anchor=CENTER)
my_tree.heading("Dadname", text="Dad Name", anchor=CENTER)
my_tree.heading("Momname", text="Mom Name", anchor=CENTER)
my_tree.heading("Phonenum", text="Phone Number", anchor=CENTER)
my_tree.heading("Sponsor", text="Sponsor", anchor=CENTER)

# Add Frame
add_frame = LabelFrame(root, text="Record", pady=10, padx=20)
add_frame.pack(pady=10)

# Command Frame
command_frame = LabelFrame(root, text="Command", pady=20, padx=20)
command_frame.pack(pady=10)

# Add Record
def add_record():
  global llist
  for record in my_tree.get_children():
    my_tree.delete(record)
  llist.push((name_entry.get(), class_entry.get(), date_entry.get(), hometown_entry.get(), dadname_entry.get(), momname_entry.get(), phonenum_entry.get(), sponsor_entry.get()))

  llist.insertList()
  
  name_entry.delete(0, END)
  class_entry.delete(0, END)
  date_entry.delete(0, END)
  hometown_entry.delete(0, END)
  dadname_entry.delete(0, END)
  momname_entry.delete(0, END)
  phonenum_entry.delete(0, END)
  sponsor_entry.delete(0, END)

# Remove Selected
def remove_selected():
  # Delete in treeview
  x = my_tree.selection() # Lấy ra những iid được chọn dạng tupple

  selected = my_tree.focus() # Lấy ra iid
  values = my_tree.item(selected, 'values')
  llist.deleteNode(values)

  for record in x:
    my_tree.delete(record)

  for record in my_tree.get_children():
    my_tree.delete(record)
  
  llist.insertList()






# Labels
name_label = Label(add_frame, text="Name")
name_label.grid(row=0, column=0, padx=20, pady=10)

class_label = Label(add_frame, text="Class")
class_label.grid(row=0, column=2, padx=20, pady=10)

date_label = Label(add_frame, text="Date")
date_label.grid(row=0, column=4, padx=20, pady=10)

hometown_label = Label(add_frame, text="Home town")
hometown_label.grid(row=0, column=6, padx=20, pady=10)

dadname_label = Label(add_frame, text="Dad name")
dadname_label.grid(row=1, column=0, padx=20, pady=10)

momname_label = Label(add_frame, text="Mom name")
momname_label.grid(row=1, column=2, padx=20, pady=10)

phonenum_label = Label(add_frame, text="Phone Number")
phonenum_label.grid(row=1, column=4, padx=20, pady=10)

sponsor_label = Label(add_frame, text="Sponsor")
sponsor_label.grid(row=1, column=6, padx=20, pady=10)

# Entry boxes
name_entry = Entry(add_frame)
name_entry.grid(row=0, column=1)

class_entry = Entry(add_frame)
class_entry.grid(row=0, column=3)

date_entry = Entry(add_frame)
date_entry.grid(row=0, column=5)

hometown_entry = Entry(add_frame)
hometown_entry.grid(row=0, column=7)

dadname_entry = Entry(add_frame)
dadname_entry.grid(row=1, column=1)

momname_entry = Entry(add_frame)
momname_entry.grid(row=1, column=3)

phonenum_entry = Entry(add_frame)
phonenum_entry.grid(row=1, column=5)

sponsor_entry = Entry(add_frame)
sponsor_entry.grid(row=1, column=7)

# Button
add_button = Button(command_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=0, padx=5)

remove_one = Button(command_frame, text="Remove Selected", command=remove_selected)
remove_one.grid(row=0, column=1, padx=5)









root.mainloop()




