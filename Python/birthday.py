#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:11:49 2023

@author: Warren Jasper

Given n people, what is the probility that two or more have birthdays
on the same day?

For n people (n < 365), 

P(n, all diff) = 365   364   363            365 - n + 1
                 --- x --- x ---  x ... x  -----------
                 365   365   365               365
                 
P(n, >= 2 duplicates) = 1 - P(n, all different))

"""

from sys import exit
import matplotlib.pyplot as plt

def main():
    
  n = int(input("Enter the number of people: "))
  if n >= 365:
    print('The probability that at least 2 people have a birthday on the same day is 1.')
    return
  p = 1.0
  for i in range(0,n):
    p *= (365 - i) / 365.
  p = 1 - p
  print('The probability that at least 2 people have a birthday on the same day is', p)
  
  
  x_vals = []
  y_vals = []
  for n in range(1,365):
    p = 1.0
    for i in range(0,n):
      p *= (365 - i) / 365.
    p = 1 - p
    x_vals.append(n)
    y_vals.append(p)
    
  plt.cla()
  plt.plot(x_vals,y_vals,label="Birthday Probabilities")
  plt.xlabel("Number of People")
  plt.ylabel("Probability")
  plt.tight_layout()
  plt.draw()
  plt.show()

if __name__ == "__main__":
  main()
