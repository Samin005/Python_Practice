import random

zone = random.randint(4, 7)
zone_conditions = {
    4: 'dx &lt; 0, dy &lt; 0, |dx| > |dy|',
    5: 'dx &lt; 0, dy &lt; 0, |dx| &lt; |dy|',
    6: 'dx > 0, dy &lt; 0, |dx| &lt; |dy|',
    7: 'dx > 0, dy &lt; 0, |dx| > |dy|',
}

print(zone, zone_conditions[zone])

zone_to_convert = random.randint(1, 3)
x = random.randint(-100, 100)
y = random.randint(-100, 100)
x_prime = x
y_prime = y
if zone == 4:
    if zone_to_convert == 1:
        x_prime = -y
        y_prime = -x
    elif zone_to_convert == 2:
        x_prime = y
        y_prime = -x
    elif zone_to_convert == 3:
        x_prime = x
        y_prime = -y
elif zone == 5:
    if zone_to_convert == 1:
        x_prime = -x
        y_prime = -y
    elif zone_to_convert == 2:
        x_prime = x
        y_prime = -y
    elif zone_to_convert == 3:
        x_prime = y
        y_prime = -x
elif zone == 6:
    if zone_to_convert == 1:
        x_prime = x
        y_prime = -y
    elif zone_to_convert == 2:
        x_prime = -x
        y_prime = -y
    elif zone_to_convert == 3:
        x_prime = y
        y_prime = x
elif zone == 7:
    if zone_to_convert == 1:
        x_prime = -y
        y_prime = x
    elif zone_to_convert == 2:
        x_prime = y
        y_prime = x
    elif zone_to_convert == 3:
        x_prime = -x
        y_prime = -y
