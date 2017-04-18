def narcissistic(x):
    n = len(x)
    total = 0
    for i in range(n):
        total += int(x[i])**n
    if total == int(x):
        return('Narcissistic.')
    else:
        return('Not narcissistic.')

while True:
    x = input('Enter a number: ')
    if len(x) != 0:
        if x.isdigit():
            print(narcissistic(x))
        else:
            print('Try again.')
    else:
        break
