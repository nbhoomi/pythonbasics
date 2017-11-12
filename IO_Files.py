#!/usr/bin/python

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

file = open('loremipsum', 'w')
for i in file:
  print i
file.close()

