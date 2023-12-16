# rainfall.py

rainfall = {
    'october ' : 3.5,
    'november': 4.2,
    'december': 2.1
}

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm total rainfall in the last quarter.\n')

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')