def withdraw(current):
    amt = int(input('Enter an amount to withdraw: '))
    if amt <= balance[current]:
        balance[current] -= amt
        print('Withdrawal successful.')
        print('New Balance:', balance[current])
    else:
        print('Insufficient funds.')

def deposit(current):
    amt = int(input('Enter an amount to deposit: '))
    balance[current] += amt
    print('Deposit successful.')
    print('New Balance:', balance[current])

def c_balance(current):
    print('Your current balance is:', balance[current])

def default(current):
    print("Invalid option")

name = ['yashwanth', 'ram', 'raj', 'manoj']
pas = [123, 456, 789, 987]
balance = [1000, 1500, 1200, 1000]

while True:
    u_n = input('Enter your name: ')
    u_p = int(input('Enter your password: '))

    for i in range(len(name)):
        if u_n == name[i] and u_p == pas[i]:
            print('Hello,', u_n)
            while True:
                print('\nOptions:')
                print('1: Withdraw\n2: Deposit\n3: Check Balance\n0: Exit')
                option = int(input('Enter option: '))
                if option == 0:
                    break
                data = {1: withdraw, 2: deposit, 3: c_balance}
                res = data.get(option, default)
                res(i)
            break
    else:
        print('User not found or incorrect password.')

    exit_choice = input('Do you want to exit? (yes/no): ')
    if exit_choice.lower() == 'yes':
        print('Thank you. Goodbye!')
        break
