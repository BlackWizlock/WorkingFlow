numbers = str(input())
countofnumbers = len(numbers)
nnn = 0
sum = 0
for number in range(countofnumbers):
  nnn = int(numbers[number])
  if nnn != 2 and nnn != 3:
    sum += nnn
print (sum)
