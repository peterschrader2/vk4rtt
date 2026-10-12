import serial
import time
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)

# Continuous reading
while True:
	line = ser.readline()
	if line:
		text = line.decode('utf-8', errors='ignore').strip()
#		print(text)
		if text:
			if "$GPGGA" in text:
				if "E,1" in text:
					print(text)
					publish.single("vk4rtt/6m_GNSS", "Locked", hostname="localhost")
				else:
					publish.single("vk4rtt/6m_GNSS", "Unlocked", hostname="localhost")



