members = int(input("How many numbers in the list: "))
list = []
for num in range(1,members+1):
    if num == 1:
        userinput = input("Enter 1 number: ")
    else:
        iteration = num
        userinput = input(f"Enter {iteration} number: ")
    list.append(num)


left = int(input("How many numbers from the left side to sum: "))
right = int(input("How many numbers from the right side to sum: "))
totalleft = 0
totalright = 0

for i in range(list[0],list[left]):
    totalleft += i

for j in list[-right:]:
    totalright += j

print(f"Sum of your left range is {totalleft}")
print(f"Sum of your right range is {totalright}")
