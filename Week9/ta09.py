print('Enter a list of numbers, type 0 when finished.')

num_input =''
nums = []

while num_input != 0:
   num_input = int(input('Enter number: '))
   if num_input == 0:
      break
   else:
      nums.append(num_input)

sum = 0
for num in nums:
   sum += num

average = sum / len(nums)

sorted_array = sorted(nums)

small_positive_num = ''
for num in sorted_array:
   if num > 0:
      small_positive_num = num
      break

print(f'The sum is: {sum}')
print(f'The average is: ' + str(round(average, 2)))
print(f'The largest number is: ' + str(sorted_array[len(sorted_array) - 1]))
print(f'The smallest positive number is: ' + str(small_positive_num))

for num in sorted_array:
   print(num)


