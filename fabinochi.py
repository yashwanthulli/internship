f0 = 0
f1 = 1
N = int(input('Enter the Length of required Fibonacci Sequence: '))
if N <= 0:
    print('Enter a Positive Integer value: ')
else:
    i = 0
    print('Fibonacci Sequence for N = ' + str(N) + ' is: ')
    while i < N:
        print(f0)
        fth = f0 + f1
        f0 = f1  # Corrected this line
        f1 = fth
        i += 1
