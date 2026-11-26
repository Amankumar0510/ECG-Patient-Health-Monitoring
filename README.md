# ECG-Based Patient Health Monitoring System

A Raspberry Pi project that reads an ECG signal through an **ADS1115** analog-to-digital converter, uploads the readings to **ThingSpeak**, and emails a PDF report.

> This is a student learning project. It is **not a medical device** and must not be used for diagnosis.

## How it works

```text
ECG signal → ADS1115 (I²C) → Raspberry Pi → ThingSpeak channel
                                          └→ PDF report by email
```

`ecg_final.py` reads one value every second and uploads it to ThingSpeak. After every 50 samples it creates a PDF report with the latest value and emails it.

## Files

| File | Purpose |
|---|---|
| `ecg_test.py` | Prints raw ADC values and voltages to check the wiring |
| `ecg_final.py` | Main program: read, upload and trigger reports |
| `send_report.py` | Creates the PDF report and sends it by email |

## Hardware

- Raspberry Pi
- ADS1115 ADC module (signal on channel A0, connected over I²C)
- ECG sensor front end

## Setup

1. Enable I²C on the Raspberry Pi (`sudo raspi-config`).
2. Install the libraries:

```bash
pip install adafruit-blinka adafruit-circuitpython-ads1x15 thingspeak reportlab
```

3. Add your own settings:
   - `ecg_final.py`: ThingSpeak channel ID, write key and the recipient's email address
   - `send_report.py`: sender email address, app password and the path for the PDF report

   Never commit real keys or passwords.

4. Check the sensor, then start the system:

```bash
python ecg_test.py
python ecg_final.py
```

## Author

**Aman Kumar**, B.Tech in Electronics & Communication Engineering
