with open("one.txt", "r") as data:
    data_items = [line.strip() for line in data]
count = 0
for index in range(len(data_items)-3):
    A = int(data_items[index]) + int(data_items[index+1]) + int(data_items[index+2])
    B = int(data_items[index+1]) + int(data_items[index+2]) + int(data_items[index+3])
    if B > A:
        count += 1
print(count)
