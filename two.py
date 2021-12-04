with open("two.txt", "r") as data:
    data_items = [line.strip() for line in data]
directions = []
for item in data_items:
    item = item.split(" ")
    directions.append(item)
x, y, z = 0, 0, 0
for num in range(len(directions)):
    if directions[num][0] == "forward":
        x = x + int(directions[num][1])
        y = y + (z * int(directions[num][1]))
    elif directions[num][0] == "up":
        z = z - int(directions[num][1])
    elif directions[num][0] == "down":
        z = z + int(directions[num][1])
print(x*y)