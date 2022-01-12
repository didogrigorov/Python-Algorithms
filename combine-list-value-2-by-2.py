arr = [1,2,3,4,5,6]

sum = 0
count = 0

for i in range(0, len(arr) // 2):
  sum = arr[i+count] + arr[i+1+count]
  count += 1
  print(sum)
