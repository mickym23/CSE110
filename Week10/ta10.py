accounts = []

print(f'\nEnter the names and balances of bank accounts (type: quit when done)')

while True:
   account_name = input('What is the name of this account? ')
   if account_name.lower() == 'quit':
      break
   balance = float(input('What is the balance? '))
   custAcc = {
         "acc_name": account_name.lower().title(),
         "acc_bal": format(balance, '.2f')
      }
   accounts.append(custAcc)

print(f'\nAccounts Information:')
for acc in accounts:
   print(f'{acc["acc_name"]} - ${acc["acc_bal"]}') 

total = 0
for acc in accounts:
   total += float(acc["acc_bal"])
print(f'\nTotal: ${total}')

average = total / len(accounts)
print(f'Average: ${str(format(average, ".2f"))}')
      
      
