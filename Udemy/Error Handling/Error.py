# Error Handling

while True:
    try:
        age = int(input('what is you age? '))
        10/age
        if age < 10:
            raise Exception('cut it out')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I\'m finally done')