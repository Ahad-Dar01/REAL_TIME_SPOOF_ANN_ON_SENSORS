#model without init effect
class Reports:
    def __init__(self):
     self.i=8
   # def ass(self):
    # print (self.i)
class Report(Reports):
    print(i=9)
    
p1=Report()
print(p1)
###c=p1.b
#print(c)
#making a child class without init and defining function using self in it imports parent class variable self instantiated
#calling without init make def fx of no use 
#defining global variable can be called in class but to assign to non self if init is not present
