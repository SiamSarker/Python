# Error Handling

while True:
    try:
        age = int(input('what is you age? '))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I\'m finally done')