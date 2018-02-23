import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_4_GPIO = 21
RELAIS_3_GPIO = 20
RELAIS_2_GPIO = 26
RELAIS_1_GPIO = 19


GPIO.setup(RELAIS_4_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

GPIO.output(RELAIS_4_GPIO, GPIO.LOW) # an
#GPIO.output(RELAIS_4_GPIO, GPIO.HIGH) # aus
GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
#GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus
GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus
#GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
