
# coding: utf-8

# In[1]:


from thegameoflife import *
import sys

print("? for console read or !f <input filename without <> >")
flag = 0
reader = "?"
writer = "?"
while (flag == 0):
    s = input()
    if len(s) >= 1:
        if s[0] != '?':
            ls = s.split()
            reader = ls[1]
            if len(ls) > 1:                
                sys.stdin = open(reader,"r")
                flag = 1
            else:
                print("Don't get you!")
                continue
        else:
            flag = 1
    else:
        print("Don't get you!")
        continue
print("? for console write or !f <output filename without <> >")
flag = 0
while (flag == 0):
    s = input()
    if len(s) >= 1:
        if s[0] != '?':
            ls = s.split()
            reader = ls[1]
            if len(ls) > 1:
                sys.stdout = open(writer,"w")
                flag = 1
            else:
                print("Don't get you!")
                continue
        else:
            flag = 1
    else:
        print("Don't get you!")
        continue
modeling()
if(reader != "?"):
    sys.stdin.close()
if(writer != "?"):
    sys.stdout.close()

