import time
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

DEVICE = "raspberry-pi"
VARIABLE1 = "l1"
VARIABLE2 = "l2"
VARIABLE3 = "l3"
VARIABLE4 = "l4"

TOKEN = "A1E-wN4jKlfbBzKMOIx1Basdc34chDSxHk8D"
while True:

	light1 = requests.get("http://things.ubidots.com/api/v1.6/devices/"+DEVICE+"/"+VARIABLE1+"/lv?token="+TOKEN)
	print "Light 1 is now : "+light1.content
        light2 = requests.get("http://things.ubidots.com/api/v1.6/devices/"+DEVICE+"/"+VARIABLE2+"/lv?token="+TOKEN)
        print "Light 2 is now : "+light2.content
        light3 = requests.get("http://things.ubidots.com/api/v1.6/devices/"+DEVICE+"/"+VARIABLE3+"/lv?token="+TOKEN)
        print "Light 3 is now : "+light3.content
        light4 = requests.get("http://things.ubidots.com/api/v1.6/devices/"+DEVICE+"/"+VARIABLE4+"/lv?token="+TOKEN)
        print "Light 4 is now : "+light4.content
	if light1=="1.0":
		GPIO.output(33,True)
        elif light1=="0.0":
                GPIO.output(33,False)

        if light2=="1.0":
                GPIO.output(11,True)
        elif light2=="0.0":
                GPIO.output(11,False)

        if light3=="1.0":
                GPIO.output(13,True)
        elif light3=="0.0":
                GPIO.output(13,False)

        if light4=="1.0":
                GPIO.output(15,True)
        elif light4=="0.0":
                GPIO.output(15,False)
	print ""
	time.sleep(1)
