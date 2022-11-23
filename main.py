# ,----,
# | DP | Copyright (C) 2022 DAREK PAGES
# '----' MIT Licence
# ==========================================================================
# File: main.py
# 
# Reading from the internal temperature sensor.
# pipico, micropython v1.19.1
#
# version: 0.3
# date: 13.11.2022 - 22.11.2022
# -------------------------------------------------------------------------
import machine
import time
import dp_filters
clb= 3.95      #calibration
cels_fahr= 1   #deegres Celsius, fahrenheit= 0
     
def deegres2fahrenheit(adc_raw, str_fah_dee= 1):
    '''Convert degrees Celsius to Fahrenheit.
        str_fah_dee==1 --> result in degrees Celsius,
        str_fah_dee==0 --> result in degrees Fahrenheit.'''
    dg= 27-((adc_raw*(3.3/65535)-0.706)/0.001721) #celsius
    if str_fah_dee==1:
        return dg
    else:
        return (dg*9/5)+32                #fahrenheit

#main:
blink= lambda tim: time.sleep(tim)        #time function sleep
print('TEMPERATURE MEASUREMENT')
tp= machine.ADC(4)
led= machine.Pin(25, machine.Pin.OUT)
sr_adc4= dp_filters.sensorfilter()        #filter object
while True:
    #fil_tp= tp.read_u16()                #raw
    fil_tp= sr_adc4.mean2(tp.read_u16(), 30)    #filter
    #fil_tp= sr_adc4.pic_correction(sr_adc4.mean2(tp.read_u16(), 30)) #filter 2 level
    rad_tp= round(deegres2fahrenheit(fil_tp, cels_fahr)-clb, 2)
    print(rad_tp)
    led.value(1)                          #LED on
    blink(0.1)
    led.value(0)                          #zLED off
    blink(0.25)
