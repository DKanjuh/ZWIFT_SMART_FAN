# ZWIFT_SMART_FAN

Installation

From sources
------------

The sources for Zwift Mobile API client can be downloaded from the `Github repo`_.

You can either clone the public repository:



    $ sudo git clone git://github.com/jsmits/zwift-client
    
   

To install Zwift Mobile API client, run this command in your terminal:

    $ cd zwift-client
    $ sudo pip install zwift-client
    $ sudo chmod 777 /home/pi/zwift-client/zwift


To install the actuel App, run this command in your terminal:

    $ sudo git clone git://github.com/DKanjuh/ZWIFT_SMART_FAN.git
    $ cd ZWIFT_SMART_FAN
    $ cp Zwift2_1.py /home/pi/zwift-client/zwift
 
Change mail and passwort
    
    $ sudo nano Zwift2_1.py

cli = Client('email','pw') in  cli = Client('Email Zwift account','passwort Zwift account) 

    
Run application

    $ sudo python Zwift2_1.py
    
Have fun !!!
    
