import psutil

disk_free = psutil.disk_usage('/').percent

print(disk_free)

