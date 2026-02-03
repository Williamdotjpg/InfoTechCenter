#Main Branch


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


#Gasoline Branch

import random
import time
from datetime import datetime, timedelta


# ---------------- Utility: Loading Animation ----------------

def loading(message, dots=3, delay=0.5):
    """
    Displays a simple loading animation in the terminal.

    Parameters:
    - message (str): Text shown before the dots
    - dots (int): Number of dots to display
    - delay (float): Time delay between dots (seconds)
    """

    print(message, end="", flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print("\n")


# ---------------- Gas & Vehicle Settings ----------------

MAX_RANGE_MILES = 400  # Max distance car can travel on a full tank


def get_gas_level():
    """
    Simulates checking the car's gas level.
    """
    time.sleep(1)  # Simulate sensor delay
    return random.randint(5, 100)


def miles_left(gas_level):
    """
    Calculates remaining miles based on gas percentage.
    """
    return (gas_level / 100) * MAX_RANGE_MILES


# ---------------- Gas Station Logic ----------------

def get_gas_stations():
    """
    Returns a list of nearby gas stations and their properties.
    """
    time.sleep(1)  # Simulate database lookup
    return [
        {"name": "QuickFuel", "distance": 8, "open": True, "slurpee": True, "snacks": True},
        {"name": "Fuel Express", "distance": 15, "open": False, "slurpee": False, "snacks": True},
        {"name": "Speedy Stop", "distance": 5, "open": True, "slurpee": False, "snacks": True},
        {"name": "Night Owl Gas", "distance": 20, "open": True, "slurpee": True, "snacks": False}
    ]


def choose_gas_station(stations):
    """
    Randomly selects one gas station.
    """
    time.sleep(1)
    return random.choice(stations)


# ---------------- Alarm Adjustment ----------------

def update_alarm_for_gas(needs_gas, base_alarm="07:00"):
    """
    Adjusts the alarm time if a gas stop is required.
    """

    alarm_time = datetime.strptime(base_alarm, "%H:%M")
    time.sleep(1)

    if needs_gas:
        alarm_time -= timedelta(minutes=20)
        print("⏰ Alarm updated to allow time for gas stop.")
    else:
        print("⏰ No alarm adjustment needed.")

    return alarm_time.strftime("%H:%M")






loading("🚘 Starting morning check")

# Step 1: Check gas level
loading("⛽ Checking gas level")
gas_level = get_gas_level()
remaining_miles = miles_left(gas_level)

print(f"⛽ Gas level: {gas_level}%")
print(f"📏 Estimated miles left: {remaining_miles:.1f} miles\n")

# Step 2: Decide if gas is needed
loading("🔍 Analyzing fuel status")
needs_gas = gas_level < 30

if not needs_gas:
    print("✅ Gas level sufficient. No stop needed.\n")
else:
    print("⚠️ Gas level low. Searching for gas stations...\n")

    # Step 3: Find a gas station
    loading("📡 Scanning nearby gas stations")
    stations = get_gas_stations()
    station = choose_gas_station(stations)

    print(f"📍 Selected station: {station['name']}")
    print(f"📏 Distance: {station['distance']} miles")

    # Step 4: Can we reach it?
    time.sleep(1)
    if remaining_miles >= station["distance"]:
        print("🚗 You can make it to this station.")
    else:
        print("❌ You cannot reach this station with current fuel!")

    # Step 5: Station status & amenities
    time.sleep(1)
    print("🏪 Checking station availability...")

    print("🟢 Station is OPEN" if station["open"] else "🔴 Station is CLOSED")
    print("🥤 Slurpees available!" if station["slurpee"] else "🚫 No Slurpees here.")
    print("🍫 Snacks available!" if station["snacks"] else "🚫 No snacks available.")

    print()

# Step 6: Update alarm
loading("⏰ Updating alarm settings")
new_alarm = update_alarm_for_gas(needs_gas)
print(f"⏰ Alarm set to: {new_alarm}\n")

print("✅ Morning gas check complete. Have a great drive! 🚗💨\n")

