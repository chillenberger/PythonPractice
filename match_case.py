

def my_match(x, y):
    match x:
        case 1 if y > 10:
            print(1)
        case 2:
            print(2)
        case _:
            print('not found ')

my_match(1, 7)