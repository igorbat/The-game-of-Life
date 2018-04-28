from thegameoflife_fortests import modeling
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
                flag = 1
            else:
                print("Don't get you!")
                continue
        else:
            flag = 1
    else:
        print("Don't get you!")
        continue
print("? for console write or ! <output filename without <> >")
flag = 0
while (flag == 0):
    s = input()
    if len(s) >= 1:
        if s[0] != '?':
            ls = s.split()
            writer = ls[1]
            if len(ls) > 1:

                flag = 1
            else:
                print("Don't get you!")
                continue
        else:
            flag = 1
    else:
        print("Don't get you!")
        continue
t = 0
q = 0
if(reader != "?"):
    sys.stdin = open(reader,"r")
    t = 1
if(writer != "?"):
    sys.stdout = open(writer,"w")
    q = 1
                
modeling(t, q)
if(reader != "?"):
    sys.stdin.close()
if(writer != "?"):
    sys.stdout.close()

