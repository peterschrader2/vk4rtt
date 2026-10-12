import psutil

ram = psutil.virtual_memory().percent

print(ram)

