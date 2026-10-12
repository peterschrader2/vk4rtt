import math
import time
import serial
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Continuous reading
while True:
	line = ser.readline()
	try:
		if line:
			text = line.decode('utf-8', errors='ignore').strip()
			if text:
				two_heat = float(text[4:9])
				publish.single("vk4rtt/Two_Heat", two_heat, hostname="localhost")
				six_heat = float(text[14:19])
				publish.single("vk4rtt/Six_Heat", six_heat, hostname="localhost")
				two_fwd = float(text[23:28]) * 0.8
				publish.single("vk4rtt/2m_forward", two_fwd, hostname="localhost")
				two_rev = float(text[30:35])
				publish.single("vk4rtt/2m_reverse", two_rev, hostname="localhost")
				six_fwd = float(text[37:42]) * 2
				publish.single("vk4rtt/6m_forward", six_fwd, hostname="localhost")
				six_rev = float(text[44:49])
				publish.single("vk4rtt/6m_reverse", six_rev, hostname="localhost")
				try:
					tor_two = math.sqrt(two_rev) / two_fwd
					two_vswr = round((1 + tor_two) / (1 - tor_two), 2)
					publish.single("vk4rtt/2m_VSWR", two_vswr, hostname="localhost")
				except:
					print("fuck_2_tor")
				try:				
					tor_six = math.sqrt(six_rev) / six_fwd
					six_vswr = round((1 + tor_six) / (1 - tor_six), 2)
					publish.single("vk4rtt/6m_VSWR", six_vswr, hostname="localhost")
				except:
					print("fuck_6_tor")
				print(two_heat, six_heat, two_fwd, two_rev, two_vswr, six_fwd, six_rev)
	except ValueError:
		print("fuck_everything")

