# Нужно написать приложение, для проверки местоположения курсора:
# *куда-то* будет отправляться информация о точных координатах курсора
import pyautogui
import time
# import sys  # может понадобиться для ОС Windows


def GetMousePosition():
    previous_position = current_position = pyautogui.position()
    try:
        while True:
            current_position = pyautogui.position()
            if current_position != previous_position:
                export = "CurrentPosition: \tx = " + str(current_position.x) + ", \ty = " + str(current_position.y) + \
                         "\nPreviousPosition: \tx = " + str(previous_position.x) + ", \ty = " + str(previous_position.y)
                print(export)
                print("Координаты текущей позиции: ", current_position[-6:], ", предыдущей: ", previous_position[-6:])
                print()
                previous_position = current_position
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n")

    print("Конечная позиция курсора: x = ", current_position.x, ", y = ", current_position.y)
    print()
    return current_position.x, current_position.y


position = GetMousePosition()
print("x =", position[0], " y =", position[1])
