xString, yString = input().split()
x = float(xString)
y = float(yString)

if x == 0 or y == 0:
    print("AXIS")

elif x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
else:
    print("Quadrant 4")