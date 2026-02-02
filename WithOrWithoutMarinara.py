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


# ---------------- Main Program ----------------

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
