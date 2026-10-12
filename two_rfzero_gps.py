import serial
import time
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM2', 115200, timeout=1)

# Continuous reading
while True:
	line = ser.readline()
	if line:
		text = line.decode('utf-8', errors='ignore').strip()
		if text:
			if "$GPGGA" in text:
				print(text)
				if "E,1" in text:
					publish.single("vk4rtt/2m_GNSS", "Locked", hostname="localhost")
				else:
					publish.single("vk4rtt/2m_GNSS", "Ublocked", hostname="localhost")




