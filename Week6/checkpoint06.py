print('Please enter a rating from 1-10 for the following:')

loan = int(input('How large is your loan? : '))
credit_history = int(input('How good is your credit history? : '))
income = int(input('How high is your income? : '))
down_payment = int(input('How large is your down payment? : '))

money_loaned = bool;

if loan >= 5:
   if credit_history >= 7 and income >= 7:
      money_loaned = True;
   elif down_payment >= 5:
      money_loaned = True;
   else: 
      money_loaned = False;
else:
   if credit_history < 4:
      money_loaned = False;
   elif (income >= 7) or (down_payment >= 7):
      money_loaned = True;
   elif (income >= 4) and (down_payment >= 4):
      money_loaned = True;
   else:
      money_loaned = False;


print(f'\n { money_loaned }')
