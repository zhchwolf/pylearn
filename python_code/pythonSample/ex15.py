# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

logfile = open(filename,"a")
print >> logfile,"\nWrite data into the file successfully."
print >> logfile,raw_input("> ")
logfile.close()