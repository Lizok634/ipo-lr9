from .isCorrectRect import isCorrectRect

class RectCorrectError(Exception):
    pass
def isCollisionRect(list1,list2):
    if not isCorrectRect(list1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(list2):
        raise RectCorrectError("2й прямоугольник некоректный")
    else:
        (x_left1,y_left1),(x_right2,y_right2)=list1
        (x_left3,y_left3),(x_right4,y_right4)=list2
    if (x_right2<x_left3 or x_left1>x_right4 or y_left1>y_right4 or y_right2<y_left3):
        return False
    return True
