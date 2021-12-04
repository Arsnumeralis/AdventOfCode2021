# PART 1
with open("three.txt", "r") as data:
    data_items = [line.strip() for line in data]
bits = len(data_items[0])
gamma = ''
epsilon = ''
big_data = [[dig for dig in item] for item in data_items]
#gamma
for i in range(bits):
    count = 0
    for big in range(len(big_data)):
        count = count + int(big_data[big][i])
    count = round(count/len(data_items))
    gamma = gamma + str(count)
gamma = int(gamma, 2)
# epsilon
for i in range(bits):
    count = 0
    for big in range(len(big_data)):
        count = count + int(big_data[big][i])
    if round(count/len(data_items)) == 1:
        count = 0
    elif round(count/len(data_items)) == 0:
        count = 1
    epsilon = epsilon + str(count)
epsilon = int(epsilon, 2)

product = gamma * epsilon
# print(product)

# PART 2
# OXYGEN
big_filtered = []
filtered = big_data
for i in range(bits):
    count_one = 0
    count_zero = 0
    for big in range(len(filtered)):
        if int(filtered[big][i]) == 1:
            count_one += 1
        else:
            count_zero += 1
    
    if count_one >= count_zero:
        filtered = [n for n in filtered if n[i] == "1"]
    else:
        filtered = [n for n in filtered if n[i] == "0"]
    if len(filtered) == 1:
        break
print(filtered)
oxygen = filtered[0]

oxygen = "".join(oxygen)

# CO2
big_filtered = []
filtered = big_data
for i in range(bits):
    count_one = 0
    count_zero = 0
    for big in range(len(filtered)):
        if int(filtered[big][i]) == 1:
            count_one += 1
        else:
            count_zero += 1
    
    if count_one >= count_zero:
        filtered = [n for n in filtered if n[i] == "0"]
    else:
        filtered = [n for n in filtered if n[i] == "1"]
    if len(filtered) == 1:
        break
print(filtered)
print(len(filtered))
co2 = filtered[0]
co2 = "".join(co2)

oxygen = int(oxygen, 2)
co2 = int(co2, 2)
prod = oxygen * co2
print(prod)


# # PART 2 NOT YET WORKING