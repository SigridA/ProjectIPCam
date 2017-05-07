import base64
import time
import urllib2

import cv2
import numpy as np

import RPi.GPIO as GPIO

usr = 'student'
pw = 'tasjekoffie'

class ipCamera(object):

    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]
        self.req = urllib2.Request(self.url)
        self.req.add_header('Authorization', 'Basic %s' % auth_encoded)
    
    def go_home(self):
	response = urllib2.urlopen(self.req)

    def get_frame(self):
        response = urllib2.urlopen(self.req)
        img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        frame = cv2.imdecode(img_array, 1)
        return frame
	
GPIO.setmode(GPIO.BCM)
button = 5
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#de led
led = 17
GPIO.setup(led, GPIO.OUT)

while True:
	input_state = GPIO.input(button)
	if input_state == False:
		content = ipCamera("http://172.23.49.1/axis-cgi/com/ptz.cgi?move=home", usr ,pw)
		print('button pressed')
		test = content.go_home()
		time.sleep(3)
		camaraIP = ipCamera('http://172.23.49.1/axis-cgi/jpg/image.cgi', usr ,pw)
		imagen_tomada=camaraIP.get_frame()
		file = "IPimage.jpg"
		cv2.imwrite(file, imagen_tomada)
