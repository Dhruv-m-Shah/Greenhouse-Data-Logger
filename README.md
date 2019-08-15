# Greenhouse Data Loggoer

Used a Raspberry Pi and Google's Drive API to make a temperature and humidity data logger for my friend's backyard greenhouse.

## Getting Started

You will need the following to replicate this project:

* [Raspberry Pi Model 3](https://www.raspberrypi.org/products/) (with Raspbian installed)
* [DTH11 Temperature and Humidity Sensor](https://www.adafruit.com/product/386)
* Breadboard or perfboard
* Monitor (And a way to connect your Raspberry Pi to it)
* Wifi connection
* Gmail account
* 1000 ohm resistor 
* Male and female jumper wires


### Installing

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python3 setup.py install
sudo pip3 install gspread
sudo pip3 install 
sudo pip3 install oauth2client
```

## Usage

Data will be logged on a google drive spreadsheet every hour(log timing can be set to your preference by modifying while loop in script.py). Every 24 hours a new google drive spreadsheet is created for recording the temperature and humidity for that day.

## What's next
- [x] Log temperature
- [x] Log humidity
- [ ] Log light intensity
- [ ] Alert user through text or email if there are abnormal readings
- [ ] Graphical user interface to allow user to change logging frequency

## Acknowledgments

* I would like to thank Kaveen Jayawardane for allowing me to incorporate a data logger for his greenhouse. Check out his [website](www.thesamakamicollection.org/).
