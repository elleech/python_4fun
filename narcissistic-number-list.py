def narcissistic_list(n):
    lst = []
    start = 10**(int(n)-1)
    end = 10**int(n)
    for i in range(start, end):
        total = 0
        convert = str(i)
        for j in range(int(n)):
            total += int(convert[j])**int(n)
            if total == i:
                lst.append(i)
    return(lst)

while True:
    n = input('How many digits? ')
    if len(n) != 0:
        if n.isdigit() and n != '0':
            result = narcissistic_list(n)
            if len(result) != 0:
                print(result)
            else:
                print('No narcissistic numbers between %d-%d.'
                      %(10**(int(n)-1), 10**int(n) - 1))
        else:
            print('Try again.')
    else:
        break
