#!/bin/python
import sys
import commands
if len(sys.argv) == 2:
	filename=sys.argv[1]
	file_op = open(filename)
	for i in filename:
		count = commands.getoutput(''' ping -ac 2 $i| grep -c error ''')	
		print ("hello " + count)
		print file_op.read()
else:
	print " argument is needed "
