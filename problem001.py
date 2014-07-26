def multiples_3_5(number):
  total = 0
  count = 0
  while count < number:
    if number % 3 == 0:
      total += number
      count += 1
    elif number % 5 ==0:
      total += number
      count += 1
    else:
      count += 1
  return total


print multiples_3_5(1000)
