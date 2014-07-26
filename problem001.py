def multiples_3_5(number):
  total = 0
  count = 0
  while count < number:
    if count % 3 == 0:
      total += count
      count += 1
    elif count % 5 == 0:
      total += count
      count += 1
    else:
      count += 1
  return total
