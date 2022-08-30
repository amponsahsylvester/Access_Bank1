import customer_account

cust = customer_account.CustomerAccount()


def welcome_screen():
    print('***** Welcome To Access Bank *******')
    user_input = int(input('1. Check Balance\n'
                           '2. Deposit\n'
                           '3. Withdraw\n'
                           '4. Cancel\n\n'
                           'Enter Your Request : '))
    user_options(user_input)


# function to display customers balance.
def user_balance():
    print(f'Balance in your account is GHC : {cust.check_balance()}')


# function to deposit into customer's account

def user_deposit():
    amount = float(input('Enter amount to be deposited : '))
    if amount > 0:
        cust.deposit(amount)
        print(f'Deposit is successful and the balance in the account is GHC:{amount}')
    else:
        print('Unable To Deposit, Try Again.')
    welcome_screen()


# function to withdraw from customer's account
def user_withdraw():
    amount = float(input('Enter Amount To Withdraw:'))
    if amount > 0:
        if cust.check_balance() < amount:
            print('Sorry, Unable to process request due to Insufficient balance.')
        else:
            cust.withdraw(amount)
        print(f'GHC:{amount} withdraw successfully, Your Balance left is GHC:{cust.check_balance()}')
    else:
        print('Unable to process request, Try Again!')


def user_options(user_input):
    if user_input == 1:
        user_balance()
        welcome_screen()
    elif user_input == 2:
        user_deposit()
        welcome_screen()
    elif user_input == 3:
        user_withdraw()
    elif user_input == 4:
        print('Thank You for working with us!')
    else:
        print('Invalid Request')
        welcome_screen()


welcome_screen()
