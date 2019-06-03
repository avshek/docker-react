#!/bin/python
import commands
from prettytable import PrettyTable 
output= commands.getoutput('''free -m | grep -i Mem | awk '{print $2}' ''')
#print "Total Memory in server is " + output + " MB"

df = commands.getoutput(' df -Ph | wc -l  ')
new_df = int(df) -1
#print  new_df

name = commands.getoutput('uname -n')
#print name 

t= PrettyTable(['servername', 'mountpoints', 'Memory (MB)'])
t.add_row([name,new_df,output])

print t 
