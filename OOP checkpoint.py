#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Question 1
class Point3D(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self) :
       return "(%d, %d, %d)" % (self.x, self.y, self.z)



my_point=Point3D(1,2,3)
print(my_point)


# In[3]:


#Question2
class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def rectangle_area(self):
        return self.length*self.width
    
    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)
        
my_rectangle = Rectangle(3,4)
print("Area of a Rectangle = ", my_rectangle.rectangle_area())
print("Perimeter of a Rectangle = ",my_rectangle.rectangle_perimeter())


# In[2]:


#Question 3
from math import pi
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter (self):
        return  2 * pi * self.r


    def area (self):
        return  pi * self.r**2
    

    # form of the cercle equation 
    def formEquation (self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    
    # method to test if given point blong to the circle or not 
    def test_belong (self, x, y):
        if (self.formEquation (x, y) == 0):
            print ("the point: (", x, y, ") belongs to the circle C")
        else:
            print ("the point: (", x, y, ") does not belong to the circle C")


# Creating of an instance object
C = Circle (1,2,1)

print ("the perimeter of the circle C is:", C.perimeter() )
print ("the area of circle C is:", C.area())
# we test if the point(1,1) belong to the circle or not
C.test_belong(1,1)


# In[5]:


#Question4
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("\n Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("\n Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("\n Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
            


# In[ ]:




