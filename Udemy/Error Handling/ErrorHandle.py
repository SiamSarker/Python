# Error handling

def sum(num1, num2):
    try:
        return num1 / num2
    # except TypeError as err:
    #     print(f'please enter numbers {err}')
    except(TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, 0))