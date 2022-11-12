try:
    Number1 = int(input("1= "))
    Number2 = int(input("2= "))    
    if Number1 > Number2:
        print('Number1 bigger than Number2')
    elif Number1 < Number2:
        print('Number1 smaller than Number2')
    else:
        print('Number1 equal to Number2')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')

