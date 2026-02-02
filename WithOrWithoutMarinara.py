#BetaTestDev Branch

#Welcome Branch
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


# ---------------- Weather Branch ----------------
# This program simulates how weather can affect
# both a morning alarm time and a car's driving behavior.

import random
from datetime import datetime, timedelta


def random_weather():
    """
    Randomly selects and returns a weather condition.
    This function simulates retrieving today's weather
    from an external weather service.
    """

    # List of all possible weather conditions the system can handle
    weather_conditions = [
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Stormy ⛈️",
        "Snowy ❄️",
        "Windy 🌬️",
        "Foggy 🌫️"
    ]

    # Randomly choose one weather condition from the list
    return random.choice(weather_conditions)


def update_alarm_based_on_weather(weather, base_alarm_time="07:00"):
    """
    Adjusts a user's alarm time based on weather conditions.

    Parameters:
    - weather (str): The detected weather condition
    - base_alarm_time (str): The original alarm time in HH:MM format

    Returns:
    - str: The updated alarm time in HH:MM format
    """

    # Convert the alarm time string into a datetime object
    # This allows us to easily add or subtract minutes
    alarm_time = datetime.strptime(base_alarm_time, "%H:%M")

    print("⏰ Alarm system: Checking weather impact on commute...")

    # Determine how much earlier the user should wake up
    # Poorer weather conditions require more buffer time
    if "Sunny" in weather or "Cloudy" in weather:
        extra_minutes = 0
    elif "Rainy" in weather or "Windy" in weather:
        extra_minutes = 15
    elif "Foggy" in weather:
        extra_minutes = 20
    elif "Snowy" in weather:
        extra_minutes = 30
    elif "Stormy" in weather:
        extra_minutes = 45
    else:
        # Fallback in case an unexpected weather string appears
        extra_minutes = 0

    # Subtract the buffer time from the original alarm
    new_alarm_time = alarm_time - timedelta(minutes=extra_minutes)

    # Display the results of the alarm calculation
    print("\n⏰ Alarm update:\n")
    print(f"   ➤ Original alarm: {base_alarm_time}\n")
    print(f"   ➤ Weather buffer: {extra_minutes} minutes\n")

    # Only show a new alarm time if a change was needed
    if extra_minutes > 0:
        print(f"   ➤ New alarm set to: {new_alarm_time.strftime('%H:%M')} ⏱️\n")
    else:
        print("   ➤ No change needed. Alarm stays the same 👍\n")

    print("✅ Alarm adjustment complete.\n")

    # Return the updated alarm time as a string
    return new_alarm_time.strftime("%H:%M")


class Car:
    """
    Represents a car that can adjust its driving
    behavior based on weather conditions.
    """

    def __init__(self):
        # Default car configuration
        self.max_speed = 120          # Maximum allowed speed in mph
        self.driving_mode = "Normal"  # Default driving mode

    def adjust_for_weather(self, weather):
        """
        Modifies the car's speed limit and driving mode
        depending on the detected weather.
        """

        print("📡 Car system: Checking weather conditions...")
        print(f"\n📡 Car system: Weather detected -> {weather}")

        # Adjust car settings to prioritize safety in bad conditions
        if "Sunny" in weather:
            self.max_speed = 120
            self.driving_mode = "Sport"
        elif "Cloudy" in weather:
            self.max_speed = 110
            self.driving_mode = "Normal"
        elif "Rainy" in weather:
            self.max_speed = 90
            self.driving_mode = "Rain"
        elif "Stormy" in weather:
            self.max_speed = 70
            self.driving_mode = "Safety"
        elif "Snowy" in weather:
            self.max_speed = 60
            self.driving_mode = "Snow"
        elif "Windy" in weather:
            self.max_speed = 85
            self.driving_mode = "Stability"
        elif "Foggy" in weather:
            self.max_speed = 75
            self.driving_mode = "Fog"

        # Output the updated car configuration
        print("\n🚗 Car response:\n")
        print(f"   ➤ Driving mode set to: {self.driving_mode}\n")
        print(f"   ➤ Max speed limited to: {self.max_speed} mph\n")
        print("✅ Adjustments complete.\n")


# ---------------- Main Program ----------------

# Generate today's weather (randomly simulated)
weather_today = random_weather()

# Display the detected weather
print("\n🌍 Today's weather:", weather_today, "\n")

# Adjust the user's alarm based on the weather
update_alarm_based_on_weather(weather_today, base_alarm_time="07:00")

# Create a Car instance
my_car = Car()

# Adjust the car's behavior according to the weather
my_car.adjust_for_weather(weather_today)

