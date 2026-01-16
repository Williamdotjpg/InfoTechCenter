# Welcome

# Libraries Imported Here
import sys
import time

# ANSI color codes
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"

print(BOLD + CYAN + "Welcome Branch - Developer: Will H" + RESET)
print("\n" + PURPLE + BOLD + "Welcome to InfoTechCenter V.1.0" + RESET)

x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = (
        YELLOW
        + "InfoTechCenter OS is Booting"
        + "." * ellipsis
        + RESET
    )
    ellipsis += 1
    
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.5)
    
    if ellipsis == 4:
        ellipsis = 0
    
    if x == 20:
        print(
            "\n"
            + BOLD
            + GREEN
            + "Operating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )
