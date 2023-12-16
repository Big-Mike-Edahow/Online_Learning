# planetary_list.py

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

print()

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.\n")

index = 0
for x in planets:
    print("The ", number[index], " planet is", planets[index], "with gravity of:", gravity_on_planets[index])
    index += 1

print()

planets.append("Pluto") # Append Pluto to planets list
print("We added Pluto to our list.")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.\n")

planets.pop()  # Goodbye, Pluto
print("Pluto just got popped off our list.")
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.\n")

print("The first planet is", planets[0])
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter")
print("Jupiter is the number", jupiter_index + 1, "planet from the sun")