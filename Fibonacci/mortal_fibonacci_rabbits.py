# -*- coding: utf-8 -*-
"""Mortal Fibonacci Rabbits

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BGJe7RRF0HIwotLX2SOH04wZ0LXFHMAa
"""



from google.colab import drive
drive.mount('/content/drive')

with open("/content/drive/MyDrive/Colab Notebooks/Rosalind/Bioinformatics Stronghold/Mortal Fibonacci Rabbits/rosalind_fibd.txt") as f:
        contents = f.read()

contents

linha=contents.split(" ")
linha
n=linha[0]
m=linha[1]
n=int(n)
m=int(m)

n ,m

def fibonacci_rabbits (n,m):
  dic={}
  for j in range (1,m+1):
    dic[j]=0
  dic[1]=1
  #print(dic)
  #print(1)
  
  if n==1:
    sum=1
  else:
    for i in range (2,n+1):
      adulto_p=0
      for j1 in range(len(dic),1,-1):
        if j1==len(dic):
          adulto_p+=dic[j1]
        dic[j1]=dic[j1-1]
        if j1>2:
          adulto_p+=dic[j1]
      dic[1]=adulto_p
  sum=0
  for chave in dic:
    sum+=dic[chave]
  #print(dic)
  return sum

soma=fibonacci_rabbits (n,m)
soma

#Trabalho realizado dia 17/12/2022
#Trabalho realizado dia 17/12/2022
#Trabalho realizado dia 17/12/2022
