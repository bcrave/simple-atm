def withdraw_cash(balance):
  while True:
    withdraw_amount = float(input('How much would you like to withdraw? $'))
    
    if withdraw_amount > balance:
      print('\nThat exceeds your current balance.\n')
    else:
      new_balance = balance - withdraw_amount
      print(f'\nYou\'ve successfully withdrawn ${withdraw_amount:.2f}\n')
      print(f'Your new balance is ${new_balance:.2f}')
      return new_balance


def deposit_cash(balance):
  deposit_amount = float(input('How much would you like to deposit? $'))
  new_balance = balance + deposit_amount
  print(f'You\'ve successfully deposited ${deposit_amount:.2f}\n')
  print(f'Your new balance is ${new_balance:.2f}')

