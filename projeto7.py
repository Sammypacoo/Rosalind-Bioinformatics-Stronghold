# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:51:07 2022

@author: user
"""

with open("C:\\Users\\user\\Downloads\\rosalind_iprb.txt") as f:
        contents = f.read()
x=contents.split("\n")
x=x[0]
x=x.split(" ")

d=int(x[0])
h=int(x[1])
r=int(x[2])


total=d+h+r


## Começando com Dominante

d_d=((d-1)/(total-1))*(1/3)
d_h=h/(total-1)*(1/3)
d_r=r/(total-1)*(1/3)


## Começando com heterozigoto

h_d=d/(total-1)*(1/3)
h_h=(((h-1)/(total-1))*(3/4))*(1/3)
h_r=(r/(total-1)*(1/2))*(1/3)


## Começando com recessivo

r_d=(d/(total-1))*(1/3)
r_h=((h/(total-1))*(2/4))*(1/3)
r_r=0

soma=d_d+d_h+d_r+h_d+h_h+h_r+r_d+r_h+r_r
