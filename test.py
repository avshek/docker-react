#!/bin/python
import commands 
Var =raw_input ( "enter the ip address  :" )
print ( " your IP is :" + Var )
count = commands.getoutput(' ping -c 2 $i| grep -c error ')
print ( count )
