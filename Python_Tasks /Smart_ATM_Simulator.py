print('Welcome To Smart ATM Simulator')

pin = 1234
balance = 5000

print('Please Enter Your Password')
entered_pin = int(input('Enter your PIN:'))

if entered_pin == pin :
    print('Correct Password')
    
    print('please Choose Your Transaction :')
    print('To Withdraw choose 1')
    print('To Check Balance choose 2')
    transaction = int(input('Enter a Number'))

    if transaction == 1:
        print('please, Enter the amount to withdraw:')
        amount = float(input("Enter the amount:"))

        if amount > balance :
            print("Sorry, your balance is insufficient.")
            print(f'Your current Balance is : {balance}')

        else :
            balance = balance - amount
            print(f"Transaction completed successfully.")
            print(f'Your current Balance is : {balance}')
            
    elif transaction == 2 :
        print(f'Your current Balance is : {balance}')

    else :
        print('you choose wrong number.')
        print('Please Try Again.')

else :
    print('Incorrect PIN. Transaction denied.')
    print('Please Try Again.')


