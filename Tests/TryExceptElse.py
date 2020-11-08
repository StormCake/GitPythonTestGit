def print_hi(name: object) -> object:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    k = int(input())
    try:
        check = 100 / k
    except ArithmeticError:
        print(f'check вылетело за границы пустоты, k было равно {k}')
    else:
        print(f'да всё норм')
