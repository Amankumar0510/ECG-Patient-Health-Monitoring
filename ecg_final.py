import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import thingspeak
from send_report import send_email

# I2C + ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

# ThingSpeak channel
channel_id = YOUR_CHANNEL_ID
write_key  = "YOUR_WRITE_KEY"
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

count = 0
print("System started...")

while True:
    value = chan.value
    print("ECG:", value)
    
    try:
        channel.update({'field1': value})
    except:
        print("ThingSpeak upload failed")

    # Har 50 samples ke baad ek email report bhejna
    count += 1
    if count % 50 == 0:
        send_email("recipient_email@example.com", value)

    time.sleep(1)
