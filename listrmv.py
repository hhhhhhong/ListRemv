#!/usr/bin/python
import sys
import math

def main():
   a = raw_input('first list').split(",")
   c = str(input('Input remove number'))
   a.remove(c)
   print('new list %s len:%d'%(str(a),len(a))) 

if __name__=='__main__':
   main()
