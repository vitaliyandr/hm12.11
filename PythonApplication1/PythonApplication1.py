try:
    Number = int(input())
    if Number == 1:
        print('Monday')
    elif Number == 2:
        print('Tuesday')
    elif Number == 3:
         print('Wednesday')
    elif Number == 4:
        print('Thursday')
    elif Number == 5:
        print('Friday')
    elif Number == 6:
        print('Saturday')
    elif Number == 7:
         print('Sunday')
    else:
        print("Error, it must be 1-7")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')

