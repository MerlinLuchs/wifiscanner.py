import subprocess

output = subprocess.check_output(("arp-scan", "-l"))
# print(output)

occupant = ["Alexis' Phone", "Moira's Phone", "David's Phone", "Johnny's Phone", "Nintendo Switch", "David's Laptop"]
address = ["xx:xx:xx:xx:xx:xx", "xx:xx:xx:xx:xx:xx", "xx:xx:xx:xx:xx:xx", "xx:xx:xx:xx:xx:xx", "xx:xx:xx:xx:xx:xx", "xx:xx:xx:xx:xx:xx"]

number = 0
print("Devices connected to wifi:")
for addresses in address:
        if addresses in str(output):
                print(occupant[number])
                number = number +1
        else:
                number = number +1
                pass
