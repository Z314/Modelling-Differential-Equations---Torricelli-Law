import numpy as np
import math as mth
from matplotlib import pyplot as plt

# Program graphs the height of fluid in a cylindrical tank, that has a hole in it, over time 
# Units for Aw, Ah, H and g should be consistent for correct output on graph (axis units on graph are same as inputted).


Aw = float(input("Input surface area of fluid in tank: "))
Ah = float(input("Input area of hole in tank: "))
H = float(input("Input height of fluid in tank when full: "))
g = float(input("Input acceleration due to gravity: "))

# time at which tank is empty, i.e., h = 0
tankEmpty = (2 * Aw * mth.sqrt(H))/(Ah * mth.sqrt(2 * g))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def h(t):
   """Calculates the value of the fluid height h.

   Arguments:
   t -- sequence of time values. 
   """
   return (1/4) * (Ah/Aw * mth.sqrt(2 * g) * t - (2 * mth.sqrt(H)))**2

t = np.linspace(0, tankEmpty, 100)

plt.title("Height of Fluid in Tank")
plt.xlabel("Time")
plt.ylabel("Height")

plt.plot(t, h(t), color='red')

plt.show()