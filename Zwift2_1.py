#!/usr/bin/env python
import random
from zwift import Client
import RPi.GPIO as GPIO
import subprocess
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_4_GPIO = 21
RELAIS_3_GPIO = 20
RELAIS_2_GPIO = 26
RELAIS_1_GPIO = 19
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

#GPIO.output(RELAIS_4_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_4_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus
GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus

Herzfrequenz=0
Herzschwelle1=115
Herzschwelle2=135
Herzschwelle3=155
Herz_Hyst=2

cli = Client('drazen@kanjuh.de','Tr1athl0n1970')
world = cli.get_world()
players = world.players
friends= players['friendsInWorld']
friend = random.choice(friends)
#player_id = friend['playerId']

# find Player_id
profile = cli.get_profile()
your_player_id = profile.latest_activity['profile']['id']
player_id = your_player_id
# end find player_id

player_state = world.player_status(player_id)
print(player_state.player_state)
print(player_state.heartrate)
while True:
    player_state = world.player_status(player_id)
    print"Herzfrequenz=",(player_state.heartrate)
    Herzfrequenz=(player_state.heartrate)
    #print"Leistung=",(player_state.power)
    #print"Trittfrequenz=",(player_state.cadence)
    #print"Speed=",(player_state.speed)
    if Herzfrequenz >= Herzschwelle1:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
        #subprocess.call("php /var/www/html/relais.php")
    else: 
        if Herzfrequenz <= (Herzschwelle1-Herz_Hyst):
            GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
            
    if Herzfrequenz >= Herzschwelle2:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # an
    else: 
        if Herzfrequenz <= (Herzschwelle2-Herz_Hyst):
            GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus       
        
    if Herzfrequenz >= Herzschwelle3:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
    else: 
        if Herzfrequenz <= (Herzschwelle3-Herz_Hyst):
            GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus       
        

