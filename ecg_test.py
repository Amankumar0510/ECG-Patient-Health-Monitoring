import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

print("Reading ECG values... (Press Ctrl+C to stop)")
while True:
    print("Value:", chan.value, "Voltage:", chan.voltage)
    time.sleep(0.5)
