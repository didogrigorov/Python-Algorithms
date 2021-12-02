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
