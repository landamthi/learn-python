colors = ["red", "green", "blue", "yellow"]
print(colors)

colors.remove("green")
print(colors)

# remove last element
colors.pop()
print(colors)
# add color
colors.insert(0,"black")
print(colors)
colors.insert(1,"purple")
print(colors)

# print(colors.index("red"))
colors = ['black', 'purple', 'red', 'blue', 'red']
print(colors)

try: 
    print("The word 'red' occurs at the following index: ", end=" ")
    print(colors.index("red"))
except:
    print("not exist")

#  find index of "red" in list
red_index = []
for i in range(len(colors)):
    if colors[i] == "red":
        red_index.append(i)
print("The word 'red' occurs at the following index: ", end=" ")
print(red_index)

# find number of occurance of "red"
print("How many times 'red' occurs: " + str(colors.count("red")))

print("Sort Example: ")
a = [1, 10, 3, 6, 5, 4, 7, 2, 9 ]
a.sort()
print(a)

# change the first element to 'dam lan'
a[0] = "Dam Lan"
print(a)