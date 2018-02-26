#!/usr/bin/env python
import random
from zwift import Client
import RPi.GPIO as GPIO
import subprocess
from flask import Flask, render_template
import datetime
app = Flask(__name__)
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
GPIO.setwarnings(False)

RELAIS_4_GPIO = 21
RELAIS_3_GPIO = 20
RELAIS_2_GPIO = 26
RELAIS_1_GPIO = 19
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

#GPIO.output(RELAIS_4_GPIO, GPIO.LOW) # an
##GPIO.output(RELAIS_4_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
##GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus
##GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
##GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {   
   19 : {'name' : 'Luefter 1', 'state' : GPIO.LOW},  
   26 : {'name' : 'Luefter 2', 'state' : GPIO.LOW},
   20 : {'name' : 'Luefter 3', 'state' : GPIO.LOW}
   #21 : {'name' : 'GPIO 21', 'state' : GPIO.LOW}   
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)






Herzfrequenz=0
Geschwindigkeit=0
Leistung=0
Herzschwelle1=115
Herzschwelle2=135
Herzschwelle3=155
Herz_Hyst=2
WSpede=0
WHerz=0
player_id=1407
cli = Client('drazen@kanjuh.de','Tr1athl0n1970')
world = cli.get_world()
players = world.players
#friends= players['friendsInWorld']
#friend = random.choice(friends)
#player_id = friend['playerId']

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('index.html', **templateData)




@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      GPIO.setup(int(pin), GPIO.IN)
      if GPIO.input(int(pin)) == True:
         response = "Pin number " + pin + " is high!"
      else:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('index.html', **templateData)


@app.route("/")
def hello():

  



   
   player_state = world.player_status(player_id)
   Herzfrequenz=(player_state.heartrate)
   Leistung=(player_state.power)
   stringspeed=player_state.speed/1000000.0
   Geschwindigkeit=('%5.1f' %(stringspeed))
   Trittfrequenz=(player_state.cadence)
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M:%S")
   print(player_state.heartrate)

   if Herzfrequenz >= Herzschwelle1:
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an       
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


   
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'heart':Herzfrequenz,
      'Vspeed':Geschwindigkeit,
      'pow':Leistung,
      'cad':Trittfrequenz,
      'pins' : pins
      }
   return render_template('index.html', **templateData)

@app.route("/")
def readpin():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('index.html', **templateData)


  

# find Player_id
#profile = cli.get_profile()
#your_player_id = profile.latest_activity['profile']['id']
#player_id = your_player_id
# end find player_id
player_state = world.player_status(player_id)
print(player_state.player_state)
print(player_state.heartrate)

   


if __name__ == "__main__":
        
   print(player_state.heartrate)
   

   app.run(host='192.168.1.206', port=5000, debug=True)

       

        
        
                    
        
