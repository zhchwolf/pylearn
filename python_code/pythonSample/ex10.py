# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line. \nHere is a ring. \a"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
This is backspace. AAA\b \r BBB
"""
j = 0
while j < 10000 :
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
#    if j%1000=0
#        print "*"
    j = j + 1

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
