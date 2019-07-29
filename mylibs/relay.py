import RPi.GPIO as GPIO

class PumpRelay:
    
    def __init__ ( self, pump_ch ):
    
        self.pump = pump_ch
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( pump_ch, GPIO.OUT, GPIO.HIGH )
    
    
    def motor_on( pin ):
        GPIO.output(pin, GPIO.LOW)  # Turn motor on
    
    
    def motor_off( pin ):
        GPIO.output(pin, GPIO.HIGH)  # Turn motor off
    
    

