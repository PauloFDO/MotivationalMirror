import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220      
timeOut = MAX_DISTANCE*60  


def pulse_in(pin,level,timeOut): 
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulse_time = (time.time() - t0)*1000000
    return pulse_time
    
def get_sonar():
    GPIO.output(trigPin,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)
    distance = pingTime * 340.0 / 2.0 / 10000.0 
    return distance
    
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

def check_if_person_is_close():  
    print('Checking for distance...')     
    while(True):
        distance = get_sonar()
       
        if distance > 10 and distance < 15:
           print('a person is in front at the distance of: ' + str(distance))
           return True                       
     
def start_distance_measurement():   
    setup()   
    return check_if_person_is_close()


    
