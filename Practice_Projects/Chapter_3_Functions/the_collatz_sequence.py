# The Collatz Sequence Page 76 Chapter 3
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

user = int(input('Enter number: '))
while user != 1:
    user = collatz(user)
