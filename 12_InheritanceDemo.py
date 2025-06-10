# we can call it as parent/base class
class parent:
    def House(self):
        print("We have House")
    def bike(self):
        print("We have bike")


class parent01:

    def car(self):
        print("We Have Car")


class child(parent, parent01):
   
   def cycle(self):
       print("We have cycle")
   
   


class grandchild(child):
    pass




# p = parent()
# p.House()

# c = child()
# c.House()
# c.bike()
# c.car()


gchild = grandchild()
gchild.House()
gchild.car()
gchild.bike()
gchild.cycle()