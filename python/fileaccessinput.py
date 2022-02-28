file = open("/home/devasc/labs/devnet-src/python/devices.txt", "a")
while True:
    newitem  = input("Type a new device to add or exit: ")
    if newitem == "exit":
        print("All done!")
        file.close()
        break
    file.write(newitem+'\n')














