# Input Validation Page 76 Chapter 3
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        user = int(input('Enter number: '))
        break  # Exit the loop if input is valid
    except ValueError:
        print('Error: You must enter an integer.')

while user != 1:
    user = collatz(user)


# We're interested in once the execution jumps to the code in the except clause, it does not return to the
# try clause.
