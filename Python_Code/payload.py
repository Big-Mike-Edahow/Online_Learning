# payload.py

from datetime import timedelta, datetime

def rocket_parts():
    print("payload, propellant, structure")

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes."
    else:
        return f"Total time to launch is {total_minutes/60} hours."
    
# Function accepts any number of keyword arguments  
def variable_length(**kwargs):
    print(kwargs)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")



print("\nRocket parts are: ")
output = rocket_parts()

print("\nDistance from Earth to Moon:", distance_from_earth("Moon"), "km.\n")

print("Days to complete mission:", round(days_to_complete(238855, 75)), "days.\n")

generate_report(80, 70, 75)
print(arrival_time("Orbit", hours=0.13))
print(arrival_time("Moon"))
print(sequence_time(4, 14, 18))

print("\nMission parameters:")
variable_length(tanks=1, day="Wednesday", pilots=3)

print()
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
print()
