total = 0

readings = " 18,27,35,20 "
readings = readings.strip()
separate = readings.split(",")

for reading in separate:
    total = total + int(reading)

average = total / len(separate)

print(total)
print(average)