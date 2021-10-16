# Letter Grade Calculator
grade = int(input('Please enter your grade percentage: '))

letterGrade = '';
if grade >= 90:
   letterGrade = 'A'
elif grade >= 80:
   letterGrade = 'B'
elif grade >= 70:
   letterGrade = 'C'
elif grade >= 60:
   letterGrade = 'D'
else:
   letterGrade = 'F'

if (grade % 10) >= 7:
   letterSign = '+'
elif (grade % 10 < 3):
   letterSign = '-'
else:
   letterSign = ''

print()

if grade >= 93:
   letterSign = ''

if letterGrade == 'F':
   letterSign = ''

print(letterGrade+letterSign)

message = ''
if grade >= 70:
   message="\nWell done! You aced it!"
else:
   message = '\nAll the best for next time, you got it!'

print(message)