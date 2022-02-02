from atm_functions import withdraw_cash, deposit_cash

balance = float(1000)
print('\n\n******Welcome to an ATM******\n\n')
print(f'Your current balance is ${balance:.2f}')

while True:
  command = input("\nWould you like to do?\n(W)ithdraw\n(D)eposit\n(C)heck balance\n(E)xit\n\n")
  if command.upper() == 'E':
    print('Goodbye')
    exit()
  
  elif command.upper() == 'W':
    balance = withdraw_cash(balance)
  elif command.upper() == 'D':
    balance = deposit_cash(balance)
  elif command.upper() == 'C':
    print(f'Your current balance is ${balance:.2f}')
  else:
    pass
  