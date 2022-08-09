import config
import socket
import json
import time
import re

#socket creation
monitor = socket.socket()
monitor.connect((config.server,config.port))

def serialize (chatlog):
	regex=re.search(r":([a-zA-Z0-9_]+).+:(.*)\r", chatlog)
	timestamp = time.time()
	user = str(regex.group(1))
	message = str(regex.group(2))
	data = {
		"username": user,
		"time": str(timestamp),
		"message": message
    	}
	
	serialized = json.dumps(data,indent=2)
	with open("chatlog.json", "a") as outfile:
		outfile.write(serialized)
	

def init():
	#twitch connection
	monitor.send(f"PASS {config.token}\n".encode('utf-8'))
	monitor.send(f"NICK {config.nickname}\n".encode('utf-8'))
	monitor.send(f"JOIN {config.channel}\n".encode('utf-8'))
	loop()

def loop():
	while(1==1):
		payload = str(monitor.recv(2048).decode('utf-8'))
		serialize(payload)

init()
