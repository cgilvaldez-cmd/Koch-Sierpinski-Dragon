# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 23:49:32 2025

@author: Carlos Gil
"""
import turtle

r1='F-G+F+G-F'
r2='GG'
teta=120

numiter = 4

for i in range(numiter):
 tem = ''
for ss in r1:
  if ss == 'F':
    tem = tem + r1
  elif ss == 'G':
    tem = tem + r2
else:
  tem = tem + ss


S= tem + r2 + tem

for ss in S:
    if ss== 'F' or ss == 'G':
     turtle.backward(30)
     turtle.right(teta)
    elif ss == '-' :
     turtle.forward(40)    
    else:
     turtle.left(teta)
     turtle.forward(30)
     turtle.backward(30)
     turtle.right(teta)


turtle.mainloop()


    
    