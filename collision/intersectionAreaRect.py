from .isCorrectRect import isCorrectRect

class ValueError(Exception):
    pass

def intersectionAreaRect(list1, list2):

    if not isCorrectRect(list1):
        raise ValueError("1-й прямоугольник некорректный")
    if not isCorrectRect(list2):
        raise ValueError("2-й прямоугольник некорректный")

    (x_left1,y_left1),(x_right2,y_right2) = list1
    (x_left3,y_left3),(x_right4,y_right4) = list2

    if x_left1 > x_right4 or y_left1 > y_right4 or x_right2 < x_left3 or y_right2 < y_left3:
        return "Площадь равна 0"
    xCross_left = max(x_left1, x_left3)
    yCross_bottom = max(y_left1, y_left3)
    xCross_right = min(x_right2, x_right4)
    yCross_top = min(y_right2, y_right4)
    crossWidth = xCross_right - xCross_left
    crossHeight = yCross_top - yCross_bottom

    square = crossWidth * crossHeight
    return f"Площадь равна {square}"
