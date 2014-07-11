#!/usr/bin/env python3.4

import sys, pickle, re
from socket import *

serverHost = 'localhost' 
serverPort = 9000

commands = []

print('commands: add, read, del, list, help, send, exit')

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

def inputcommands():
	a = input('>')

	if a.split(' ')[0] == 'help':
		print('command add:  "add key  value")')
		print('command read: "read key"')
		print('command del:  "del key"')
		print('command list: show all')
		print('command send: send command/commands to server')
		print('command exit: "exit"')
		inputcommands()

	if a.split(' ')[0] == '':
		inputcommands()

	if a.split(' ')[0] == 'add':
		try:
			commands.append(['add', a.split(' ')[1], a.split(' ')[2]])
			inputcommands()
		except IndexError as i:
			print('bad command')
			inputcommands()

	if a.split(' ')[0] == 'del':
		commands.append(['del', a.split(' ')[1]])
		inputcommands()

	if a.split(' ')[0] == 'read':
		commands.append(['read', a.split(' ')[1]])
		inputcommands()

	if a.split(' ')[0]== 'list':
		commands.append(['list'])
		inputcommands()

	if a.split(' ')[0] == 'exit':
		sockobj.close()
		sys.exit()

	if a.split(' ')[0] == 'send':
		
		sockobj.send(pickle.dumps(commands))
		data = sockobj.recv(1024)

		for i in  pickle.loads(data):
			print(''.join(i))
		del commands[:]
		inputcommands()

	else: 
		print('enter command')
		inputcommands()

if __name__ == '__main__':
	inputcommands()
