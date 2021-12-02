data = [5,1,4,9,3,11,8,10,12,2,4,6,7]

for scanIndex in range(0,len(data)):
  minIndex = scanIndex
  for compIndex in range(scanIndex + 1, len(data)):
    if data[compIndex] < data[minIndex]:
      minIndex = compIndex
  if minIndex != scanIndex:
      data[scanIndex], data[minIndex] = \
          data[minIndex], data[scanIndex]
      print(data)

"""
Output:
[1, 5, 4, 9, 3, 11, 8, 10, 12, 2, 4, 6, 7]
[1, 2, 4, 9, 3, 11, 8, 10, 12, 5, 4, 6, 7]
[1, 2, 3, 9, 4, 11, 8, 10, 12, 5, 4, 6, 7]
[1, 2, 3, 4, 9, 11, 8, 10, 12, 5, 4, 6, 7]
[1, 2, 3, 4, 4, 11, 8, 10, 12, 5, 9, 6, 7]
[1, 2, 3, 4, 4, 5, 8, 10, 12, 11, 9, 6, 7]
[1, 2, 3, 4, 4, 5, 6, 10, 12, 11, 9, 8, 7]
[1, 2, 3, 4, 4, 5, 6, 7, 12, 11, 9, 8, 10]
[1, 2, 3, 4, 4, 5, 6, 7, 8, 11, 9, 12, 10]
[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 11, 12, 10]
[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 12, 11]
[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
