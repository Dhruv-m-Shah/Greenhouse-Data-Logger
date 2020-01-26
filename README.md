# Greenhouse Data Logger

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

## Device in Action
![DSC_0592](https://user-images.githubusercontent.com/42727015/63071603-f2b53800-beed-11e9-8729-f1886ba204f8.JPG)
![DSC_0606](https://user-images.githubusercontent.com/42727015/63071746-7a02ab80-beee-11e9-9d16-2113809b0d4e.JPG)
![DSC_0608](https://user-images.githubusercontent.com/42727015/63071907-204eb100-beef-11e9-9403-30da0b6c3d11.JPG)



## What's next
- [x] Log temperature
- [x] Log humidity
- [ ] Log light intensity
- [ ] Alert user through text or email if there are abnormal readings
- [ ] Graphical user interface to allow user to change logging frequency




## Acknowledgments

* I would like to thank Kaveen Jayawardane for allowing me to incorporate a data logger for his greenhouse.
