#Welcome

#Libraries Imported Here
import sys
import time

print("Welcome Branch - Developer: Will H")
print("\nWelcome to InfoTechCenter V.1.0")
print("\nInfoTechCenter is Booting Up...")

x = 0
ellipsis = 0

while x != 20:
    x += 1  #or x = x+1
    ellipsisMessage = ("InfoTechCenter OS is Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + ellipsisMessage)
    time.sleep(.5)
    if ellipsis == 4:
         ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")
    
