# planetary_gravity.py

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

planets_before_earth = planets[0:2]
print("Planets before Earth: ", planets_before_earth)

print()

planets_after_earth = planets[3:8]
print("Planets after Earth: ",planets_after_earth)

print()

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

print()

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
print()
regular_satellite_moons.sort()
print("The sorted regular satellite moons of Jupiter are", regular_satellite_moons)
print()
regular_satellite_moons.sort(reverse=True)
print("The reverse sorted regular satellite moons of Jupiter are", regular_satellite_moons)