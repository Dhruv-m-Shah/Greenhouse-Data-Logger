import sys
import Adafruit_DHT
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

#configure Adafruit sensor
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#END configure Adafruit sensor

#Set scope and credentials for google sheets
scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('greenhouse-506f0f5ea30a.json', scope) #Make service account from google API keys console and download .json credential file
gc = gspread.authorize(credentials)
#END set scope and credentials for google sheets

hour = -1
day = -1
def new_day():
    if(time.localtime(time.time())[3] == 0):
        return True
    else:
        return False
def setup_new_worksheet():
    wks.append(['Time', 'Temperature', 'Humidity'])
    
def new_hour():
    if(time.localtime(time.time())[4] == 0):
        return True
    else:
        return False

def setup_new_worksheet():
    wks.append_row(['Time', 'Temperature', 'Humidity'])
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 
    wks.append_row([str(new_time()), str(temperature), str(humidity)])

def new_time():
    return time.localtime(time.time())[3]


localtime = time.asctime(time.localtime(time.time()))
sh = gc.create(localtime)
time.sleep(20)
sh.share('backyard.green.house.data@gmail.com', perm_type = 'user', role = 'writer')
time.sleep(20)
wks = gc.open(localtime).sheet1
setup_new_worksheet()
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
wks.append_row([str(new_time()), str(temperature), str(humidity)])
hour = new_time()


while(True):
    gc.login()
    time.sleep(10)
    if(new_day() and day != time.localtime(time.time())[2]):
        gc.login()
        time.sleep(20)  #Time.sleeps are used to ensure above line of code  has executed before running next line of code.
        gc = gspread.authorize(credentials)
        time.sleep(10) 
        localtime = time.asctime(time.localtime(time.time()))
        sh = gc.create(localtime)
        time.sleep(20)
        sh.share('backyard.green.house.data@gmail.com', perm_type = 'user', role = 'writer')
        time.sleep(20)
        wks = gc.open(localtime).sheet1
        setup_new_worksheet()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 
        wks.append_row([str(new_time()), str(temperature), str(humidity)])
        day = time.localtime(time.time())[2]
                                 
    if(new_hour() and hour != time.localtime(time.time())[3]):
        gc = gspread.authorize(credentials)
        time.sleep(20)
        gc.login()
        time.sleep(20)
        wks = gc.open(localtime).sheet1
        time.sleep(20)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 
        wks.append_row([str(new_time()), str(temperature), str(humidity)])
        hour = new_time()
