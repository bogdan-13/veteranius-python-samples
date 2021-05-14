for count in range(1, 101):
    if count % 3 == 0 and count % 5 == 0:
        print('Fizz-Buzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('Buzz')
    else:
        print(count)
