# countdown.py

from datetime import date
from time import sleep

print("\nStardate:", date.today(), "\n")
sleep(2)

print("Coundown commencing. Fire One.\n")
sleep(2)

print("T-6 Seconds...")
sleep(1)

countdown = [5, 4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("\nSolid rocket booster ignition and liftoff!!!!  🚀\n")
