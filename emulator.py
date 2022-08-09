from json import JSONDecoder
import json
from PIL import Image, ImageFont, ImageDraw
from functools import partial
import re
import cv2
import os

MAX_STACK = 8
FONT_SIZE=8
chat_stack = []
frame_count=0

class chat:
	def __init__(self, user, timestamp, message):
		self.user = user
		self.timestamp = timestamp
		self.message  = message

def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
	buffer = ''
	for chunk in iter(partial(fileobj.read, buffersize), ''):
		buffer += chunk
		while buffer:
			try:
				result, index = decoder.raw_decode(buffer)
				yield result
				buffer = buffer[index:].lstrip()
			except ValueError:
				break

def to_chat(payload):
	regex=re.search(r".*{'username': '(.*)', 'time'(.*)', 'message': '(.*)'}", payload)
	obj = chat(str(regex.group(1)),str(regex.group(2)),str(regex.group(3)))
	return obj

def gen_frame(payload):
	global frame_count, MAX_STACK, FONT_SIZE, chat_stack
	frame_count = frame_count + 1
	if len(chat_stack) >=MAX_STACK:
		chat_stack.pop(0)
	chat_stack.append(payload)
	img = Image.new("RGB", (500,150),"green")
	font = ImageFont.load_default()
	draw = ImageDraw.Draw(img)
	spacing= FONT_SIZE/2 + FONT_SIZE
	for c in chat_stack:
		drawable = c.user + ': ' + c.message 
		draw.text((0, spacing),drawable.encode('utf-8'),(255,255,255),font=font)
		spacing = spacing + FONT_SIZE/2 + FONT_SIZE
	filename = str(frame_count)  + '.jpg'
	savepath = 'images/'
	completeName = os.path.join(savepath, filename)
	img.save(completeName)

with open('chatlog.json', 'r') as chatz:
	for data in json_parse(chatz):
		data=to_chat(str(data))
		gen_frame(data)
		
images = [img for img in os.listdir('images/') if img.endswith(".jpg")]
frame = cv2.imread(os.path.join('images/', images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter('video.avi', 0, 1, (width,height))

for image in images:
	video.write(cv2.imread(os.path.join('images/', image)))

cv2.destroyAllWindows()
video.release()
