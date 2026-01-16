# Welcome
# This is the entry point of the program

# Libraries Imported Here
import sys          # Used for low-level terminal output control
import time         # Used to add delays for animation timing

# ANSI color codes
GREEN = "\033[32m"  # Green text (used for success messages)
CYAN = "\033[36m"   # Cyan text (used for headers)
YELLOW = "\033[33m" # Yellow text (used for boot/status messages)
RED = "\033[31m"    # Red text (unused here, reserved for errors)
RESET = "\033[0m"   # Resets text color/style back to default
BOLD = "\033[1m"    # Makes text bold
PURPLE = "\033[35m" # Purple text (used for version branding)

# Prints the developer banner in bold cyan
print(BOLD + CYAN + "Welcome Branch - Developer: Will H" + RESET)

# Prints the application name and version in bold purple
print("\n" + PURPLE + BOLD + "Welcome to InfoTechCenter V.1.0" + RESET)

# Counter to control how long the boot animation runs
x = 0

# Counter to control how many dots appear in the boot message
ellipsis = 0

# Loop runs until x reaches 20 (simulates boot duration)
while x != 20:
    x += 1  # Increment loop counter

    # Build the boot message with animated dots
    ellipsisMessage = (
        YELLOW                              # Set text color to yellow
        + "InfoTechCenter OS is Booting"    # Base boot text
        + "." * ellipsis                   # Add dots for animation
        + RESET                             # Reset terminal formatting
    )

    ellipsis += 1  # Increase dot count

    # '\r' moves cursor to start of line
    # '\033[K' clears the current line
    # This allows overwriting the same line repeatedly
    sys.stdout.write("\r\033[K" + ellipsisMessage)

    # Forces the terminal to immediately display the updated line
    sys.stdout.flush()

    # Pause for half a second to control animation speed
    time.sleep(0.5)

    # Reset dots back to zero after reaching 3
    if ellipsis == 4:
        ellipsis = 0

    # When the loop finishes, print the success message
    if x == 20:
        print(
            "\n"
            + BOLD
            + GREEN
            + "Operating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )
