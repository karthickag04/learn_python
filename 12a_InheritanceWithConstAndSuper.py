# we can call it as parent/base class
class parent:

    def __init__(self, parent_name):
        self.parent_name = parent_name
    
    def House(self):
        return "House"

    def bike(self):
        print("We have bike")

    def get_parent_name(self):
        return self.parent_name




class child(parent):
     
    def __init__(self,parent_name, child_name):

        super().__init__(parent_name) 

        self.child_name = child_name
    
    def cycle(self):
       print("We have cycle")

    def House(self):
        # return super().House() 
        old_house = super().House()


        p = parent(super().get_parent_name())
        old_housename = p.House()

        print("Printed using object " , old_housename)
        print("Printed using super " , old_house)

        print("Hi this is .. parent name ", super().get_parent_name())
        print("Hi this is child name .. ", self.child_name)

        return "Renovated House"
   
   

c = child("Ragu", "ragavan")
print("I can use my paremt .. ", c.House())