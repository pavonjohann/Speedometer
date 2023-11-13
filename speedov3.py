#official tester 1
from machine import ADC
import time

measure1 = ADC(28)
measure2 = ADC(27)
ms1 = 0
ms2 = 0

for i in range(2000):
    measurement1 = measure1.read_u16()
    measurement2 = measure2.read_u16()
    
    if measurement1 < 40000:
        ms1 = time.ticks_ms()
    if measurement2 < 30000:
        ms2 = time.ticks_ms()
        time_secs1 = ms1/1000
        time_secs2 = ms2/1000
        dis_met = 0.275
        velocity = dis_met/abs(time_secs1 - time_secs2)
        if velocity > 0.37:
            print(f'Eastward lap velocity:{velocity:,.2f} m/s.\n')
    if measurement2 < 30000:
        ms2 = time.ticks_ms()
    if measurement1 < 40000:
        ms1 = time.ticks_ms()
        time_secs1 = ms1/1000
        time_secs2 = ms2/1000
        dis_met = 0.275
        velocity = dis_met/abs(time_secs2 - time_secs1)
        if velocity > 0.37:
            print(f'Westward lap velocity:{velocity:,.2f} m/s.\n')
    time.sleep(0.01)
    
    
    
    
while True:
    if speed.read_u16() > 30000:
        dir_b.duty_u16(0)
        dir_a.duty_u16(speed.read_u16())
    else:
        dir_a.duty_u16(0)
        dir_b.duty_u16(65535-speed.read_u16()) 
    print(speed.read_u16())
    time.sleep(0.01)
    
        
