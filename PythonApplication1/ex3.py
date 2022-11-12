try:
    Number = int(input())
    if Number < 0:
        print("Numbe is negative")
    elif Number > 0:
        print("Number is positive")
    elif Number == 0:
        print("Number is equal to zero")
    else:
        print('Error')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
