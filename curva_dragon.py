# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 13:58:09 2025

@author: Carlos Gil
"""

import turtle

r1 = 'F-G+F+G-F'
r2 = 'GG'
angle = (90)

numiter = 10

for i in range(numiter):
  tem = ''
for ss in r1:
  if ss == 'F':
    tem = tem + r1
  elif ss == 'G':
    tem = tem + r2
else:
  tem = tem + ss

S = tem + r2 + tem

for ss in S:
    if ss == 'F' or ss == 'G':
      turtle.forward(30)
      turtle.right(angle)
    elif ss == '-':
      turtle.backward(30)
    else:
      turtle.left(angle)
      turtle.forward(30)
      turtle.right(angle)
      turtle.backward(30)
      
      
turtle.mainloop()