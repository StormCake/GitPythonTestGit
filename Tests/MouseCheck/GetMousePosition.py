# Нужно написать приложение, для проверки местоположения курсора фунцкия выдает информацию о координатах курсора
# Также было бы хорошо сделать это демоном
from pyautogui import position
from time import sleep
# import sys  # может понадобиться для ОС Windows


def GetMousePosition():
    previous_position = current_position = position()
    try:
        while True:
            current_position = position()
            if current_position != previous_position:
                export = "CurrentPosition: \tx = " + str(current_position.x) + ", \ty = " + str(current_position.y) + \
                         "\nPreviousPosition: \tx = " + str(previous_position.x) + ", \ty = " + str(previous_position.y)
                print(export)
                print("Координаты текущей позиции: ", current_position[-6:], ", предыдущей: ", previous_position[-6:])
                print()
                previous_position = current_position
            sleep(0.5)
    except KeyboardInterrupt:
        print("\n")

    print("Конечная позиция курсора: x = ", current_position.x, ", y = ", current_position.y)
    print()
    return current_position.x, current_position.y


CursorPosition = GetMousePosition()
print("x =", CursorPosition[0], " y =", CursorPosition[1])
