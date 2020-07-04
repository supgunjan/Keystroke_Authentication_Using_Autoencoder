from __future__ import print_function

import pyxhook
import time
import json
import sys
import csv
import itertools

special = {
	'!' : 'exclam',
	'@' : 'at', 
	'#' : 'numbersign',
	'$' : 'dollar',
	'%' : 'percent',
	'^' : 'asciicircum',
	'&' : 'ampersand',
	'*' : 'asterisk',
	'(' : 'parenleft',
	')' : 'parenright',
	'_' : 'underscore',
	'{' : 'braceleft',
	'}' : 'braceright',
	'[' : 'bracketleft',
	']' : 'bracketright',
	'~' : 'asciitilde',
	'`' : 'grave',
	'-' : 'minus',
	'=' : 'equal',
	'+' : 'plus',
	'|' : 'bar',
	';' : 'semicolon',
	':' : 'colon',
	'.' : 'period',
	'<' : 'less',
	'>' : 'greater',
	'?' : 'question',
	',' : 'comma'
}

frequency = 0
if len(sys.argv) == 1:
	frequency = 1
else :
	frequency = int(sys.argv[1])

filename = sys.argv[2]
user = input("UserName : ")
password = input("Password : ")

print("Frequecy : {0}".format(frequency))

all_features = [] # contains all rows
key_pressed = 0

username_password = [user, password]
down_time = []
up_time = []

up = False

def get_flight_dwell(down_time, up_time):
	flight_time = []
	dwell_time = []

	for i in range(len(down_time)):
		#print(i)
		dwell_time.append(up_time[i] - down_time[i])

	for i in range(1, len(down_time)):
		flight_time.append(down_time[i] - up_time[i - 1])

	return flight_time, dwell_time


def kb_down_event(event):
	global key_pressed, up
	try:
		print("Down Time {0} : {1}".format(event.Key, time.time()))
		if key_pressed < len(password):
			x = password[key_pressed]
			if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
				pass				
			elif(x >= '0' and x <= '9'):
				pass
			else:
				x = special[x]
	
		if event.Key != 'Return' and event.Key != 'BackSpace' and key_pressed < len(password) and x == event.Key:
			down_time.append(time.time())
			key_pressed = key_pressed + 1
			up = True
		else:
			print(event.Key)
	except KeyError:
		pass

def kb_up_event(event):
	global key_pressed, up
	try:
		print("Up Time {0} : {1}".format(event.Key, time.time()))
		if key_pressed - 1 < len(password):
			x = password[key_pressed - 1]
			if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
				pass
			elif(x >= '0' and x <= '9'):
				pass
			else:
				x = special[x]

		if up:
			up_time.append(time.time())
			up = False
		else:
			print(event.Key)
	except KeyError:
		pass

hookman = pyxhook.HookManager()

hookman.KeyDown = kb_down_event

hookman.KeyUp = kb_up_event

hookman.HookKeyboard()

hookman.start()

password_entry_count = 1
ok = True
while password_entry_count <= frequency:
	print("enter {} times more!".format(1+frequency - password_entry_count))
	input_pwd = input("Enter \'{}\' : ".format(password))
	is_pwd_correct = False
	if input_pwd == password:
		print("Password Correct")
		is_pwd_correct = True
		key_pressed = 0

	if is_pwd_correct:
		password_entry_count += 1
		print("Down time : {0}".format(down_time))
		print("Up time : {0}".format(up_time))
		flight_time, dwell_time = get_flight_dwell(down_time, up_time)
		tmp = itertools.chain(username_password, flight_time, dwell_time)
		print(tmp)
		all_features.append(tmp)
		print("Flight time : {0}".format(flight_time))
		print("Dwell time : {0}".format(dwell_time))
		down_time.clear()
		up_time.clear()
	else :
		ok = False
		print("Please try again")
		break


hookman.cancel()
print(all_features)
if ok:
# 	#put in csv
	path = './dataset/' + filename
	with open(path, 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(all_features)





