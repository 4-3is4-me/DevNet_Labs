devices = []
file = open("/home/devasc/labs/devnet-src/python/devices.txt", "r")
for i in file:
    i = i.strip()
    devices.append(i)
    print(devices)

file.close()