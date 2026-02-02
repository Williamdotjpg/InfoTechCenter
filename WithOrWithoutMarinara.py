#Gasoline Branch


import random
from datetime import datetime, timedelta


# ---------------- Gas & Vehicle Settings ----------------

# Maximum distance (in miles) the car can travel on a full tank
MAX_RANGE_MILES = 400


def get_gas_level():
    """
    Simulates checking the car's gas level.

    Returns:
    - int: Gas level percentage (0–100)
    """

    # Random gas level to simulate real-world variation
    return random.randint(5, 100)


def miles_left(gas_level):
    """
    Calculates how many miles the car can still travel.

    Parameters:
    - gas_level (int): Current gas level percentage

    Returns:
    - float: Estimated remaining miles
    """

    # Gas level is a percentage of the max range
    return (gas_level / 100) * MAX_RANGE_MILES


# ---------------- Gas Station Logic ----------------

def get_gas_stations():
    """
    Creates a list of nearby gas stations.
    Each station includes distance and amenities.

    Returns:
    - list of dicts: Gas station data
    """

    return [
        {
            "name": "QuickFuel",
            "distance": 8,
            "open": True,
            "slurpee": True,
            "snacks": True
        },
        {
            "name": "Fuel Express",
            "distance": 15,
            "open": False,
            "slurpee": False,
            "snacks": True
        },
        {
            "name": "Speedy Stop",
            "distance": 5,
            "open": True,
            "slurpee": False,
            "snacks": True
        },
        {
            "name": "Night Owl Gas",
            "distance": 20,
            "open": True,
            "slurpee": True,
            "snacks": False
        }
    ]


def choose_gas_station(stations):
    """
    Randomly selects one gas station from the list.

    Parameters:
    - stations (list): Available gas stations

    Returns:
    - dict: Selected gas station
    """

    return random.choice(stations)


# ---------------- Alarm Adjustment ----------------

def update_alarm_for_gas(needs_gas, base_alarm="07:00"):
    """
    Updates the alarm time if a gas stop is required.

    Parameters:
    - needs_gas (bool): Whether the car needs gas
    - base_alarm (str): Original alarm time (HH:MM)

    Returns:
    - str: Updated alarm time
    """

    alarm_time = datetime.strptime(base_alarm, "%H:%M")

    # If gas is needed, wake up earlier to allow time to stop
    if needs_gas:
        alarm_time -= timedelta(minutes=20)
        print("⏰ Alarm updated due to gas stop.")
    else:
        print("⏰ No alarm change needed.")

    return alarm_time.strftime("%H:%M")


# ---------------- Main Program ----------------

print("\n🚘 Starting Morning Gas Check...\n")

# Step 1: Get gas level
gas_level = get_gas_level()
remaining_miles = miles_left(gas_level)

print(f"⛽ Gas level: {gas_level}%")
print(f"📏 Estimated miles left: {remaining_miles:.1f} miles\n")

# Step 2: Decide if gas is needed
needs_gas = gas_level < 30

if not needs_gas:
    print("✅ Gas level is sufficient. No need to stop for gas.\n")
else:
    print("⚠️ Gas level is low. Looking for gas station...\n")

    # Step 3: Pick a gas station
    stations = get_gas_stations()
    station = choose_gas_station(stations)

    print(f"📍 Selected station: {station['name']}")
    print(f"📏 Distance: {station['distance']} miles")

    # Step 4: Check if we can reach it
    if remaining_miles >= station["distance"]:
        print("🚗 You can make it to this gas station.")
    else:
        print("❌ You cannot reach this station with current gas!")

    # Step 5: Check station availability and amenities
    if station["open"]:
        print("🟢 Station is OPEN")
    else:
        print("🔴 Station is CLOSED")

    if station["slurpee"]:
        print("🥤 Slurpees available!")
    else:
        print("🚫 No Slurpees here.")

    if station["snacks"]:
        print("🍫 Snacks available!")
    else:
        print("🚫 No snacks available.")

    print()

# Step 6: Update alarm
new_alarm = update_alarm_for_gas(needs_gas)
print(f"⏰ Alarm set to: {new_alarm}\n")

print("✅ Morning gas check complete.\n")
