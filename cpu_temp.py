import psutil

temps = psutil.sensors_temperatures()
#print(temps)

CPU_temp = temps['cpu_thermal'][0].current

print(round(CPU_temp, 0))

