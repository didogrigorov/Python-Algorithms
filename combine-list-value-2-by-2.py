numbers = list(input("Enter even number of digits: "))

for item in range(0, len(numbers)):
  numbers[item] = int(numbers[item])

print(numbers)
sum = 0
count = 0

for i in range(0, len(numbers) // 2):
  sum = numbers[i+count] + numbers[i+1+count]
  count += 1
  print(sum)
