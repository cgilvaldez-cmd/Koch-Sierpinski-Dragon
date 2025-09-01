# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 21:15:25 2025

@author: Carlos Gil
"""
import turtle

r1 = 'F-F+F' 
r2 = 'F+F-F' 
angle = 90

numiter = 4

for i in range(numiter):
  tem = ''
for ss in r1:
  if ss == 'F':
    tem = tem + r1
  elif ss == 'F':
    tem = tem + r2
else:
  tem = tem + ss
  
  S= tem + r1 + r2

for ss in S:
    if ss == 'r1' or ss == 'r2':
        turtle.forward(30)
        turtle.right(angle)
        turtle.back(30)
    elif ss == '-':
        turtle.left(angle)
        turtle.forward(30)
        turtle.right(angle)
        turtle.backward(30)
    else:
        turtle.right(angle)
        turtle.forward(30)
        turtle.left(angle)
        turtle.backward(30)
        turtle.right(angle)
        turtle.forward(30)
        
        
turtle.mainloop()
window.exitonclick()    
  
    

