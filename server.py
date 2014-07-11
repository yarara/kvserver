#!/usr/bin/env python3.4

from socket import *
import _thread as thread
import time, pickle

MyHost = ''
MyPort = 9000
MyDict = {}
response = []

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((MyHost, MyPort))
sockobj.listen(5)

def now():
	return time.ctime(time.time())

def commands(request):

	for command in request:
		if command[0] == 'add':
			MyDict[command[1]] = command[2]
			response.append(['added ', command[1], ' -> ', command[2]])

		if command[0] == 'del':
			del MyDict[command[1]]
			response.append(['deleted ', command[1]])

		if command[0] == 'read':			
			response.append(command[1], ' -> ', MyDict.get(command[1]))

		if command[0] == 'list':
			temp_dict = []
			for i, j in MyDict.items():
				response.append([i, ' -> ', j])

	return response		

def handleClient(connection):

	while True:
		data = connection.recv(1024)
		if not data: break
		commands(pickle.loads(data))
		connection.send(pickle.dumps(response))

		if len(response) > 0:
			del response[:]

	connection.close()

def dispatcher():

	while True:

		connection, address = sockobj.accept()

		print('Server connected by', address, end=' ') 
		print('at', now())
		thread.start_new_thread(handleClient, (connection,))

if __name__ == '__main__':
	dispatcher()
