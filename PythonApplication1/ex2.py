try:
    Number = int(input())
    if Number == 1:
        print('January')
    elif Number == 2:
        print('February')
    elif Number == 3:
         print('March')
    elif Number == 4:
        print('April')
    elif Number == 5:
        print('May')
    elif Number == 6:
        print('June')
    elif Number == 7:
         print('July')
    elif Number == 8:
         print('August')
    elif Number == 9:
         print('September')
    elif Number == 10:
         print('October')
    elif Number == 11:
         print('November')
    elif Number == 12:
         print('December')
    else:
        print("Error, it must be 1-12")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
