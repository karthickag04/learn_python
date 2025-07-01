# we can call it as parent/base class
class parent:

    def House(self):
        print("We have House frm parent")


    def bike(self):
        print("We have bike")




class parent01:

    def car(self):
        print("We Have Car")


class child(parent, parent01):
     
     
     def House(self):
         super().House()
         print("I have House too from child class")
   
   
class child1(parent, parent01):
     
     
     def House(self):
         super().House()
         print("I have House too from child class")
   
   
class child2(parent, parent01):
     
     
     def House(self):
         super().House()
         print("I have House too from child class")
   
   
class child3(parent, parent01):
     
     
     def House(self):
         super().House()
         print("I have House too from child class")
   
   


class grandchild(child):
    pass

childObj = grandchild()
childObj.House()
childObj.bike()
childObj.car()


# p = parent()
# p.House()

# c = child()
# c.House()
# c.bike()
# c.car()


# gchild = grandchild()
# gchild.House()
# gchild.car()
# gchild.bike()
# gchild.cycle()