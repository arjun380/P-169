
from tkinter import *




from tkinter import messagebox







root = Tk()


root.geometry("900x600")


root.title("Classes")







class CreateElements:


  


   def __init__(self):


       print("This is CreateElements class")


      


   def createNewLabel(self):


       label = Label(root,text = "A new label is been created using class", fg="#ff1100")


       label.pack()


   def createButton(self):


       class_btn = Button(root, text ="Button", command = self.message)


       class_btn.pack(padx=20, pady = 10)


   def createDropdown(self):


       value = [1,2,3,4]


       class_dropdown = tkk.Combobox(root,state="readonly", values = value)


  


def choose(self):


   global dropdown


   element = dropdown.get()


   if(element == "Label"):


       self.createLabel()


   elif(element == "Button"):


       self.createButton()


   elif(element == "Dropdown"):


       self.createDropdown()


              


def message(self):


   messagebox.showinfo("showinfo", "You clicked the button created using class")







obj_of_CreateElements = CreateElements()







btn = Button(root, text="Click to create label and button  element", command =   obj_of_CreateElements.createNewElement)


btn.pack(padx=20, pady = 10)







root.mainloop()


