#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ionyshchenko
#
# Created:     02.04.2015
# Copyright:   (c) ionyshchenko 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fname=input("Enter file name:")
#set default file
if len(fname)<1 :
    fname="D:\Python\mbox-short.txt"
    
fhandle=open(fname)
hour_list=dict()
for line in fhandle:
    if line.startswith("From "):
        words=line.split()
        time=words[5]
        pos=time.find(":")
        hours=time[:pos]
        hour_list[hours]=hour_list.get(hours,0)+1

h_lst=list()
for k,v in hour_list.items():
    h_lst.append((k,v))

h_lst.sort()

for k,v in h_lst:
    print(k,v)

