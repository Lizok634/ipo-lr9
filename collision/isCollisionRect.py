from .isCorrectRect import isCorrectRect
from .RectCorrectError import RectCorrectError

def isCollisionRect(rect1, rect2):
     
    if not isCorrectRect(rect1): 
        raise RectCorrectError("1й прямоугольник некоректный.") 
    if not isCorrectRect(rect2): 
        raise RectCorrectError("2й прямоугольник некоректный.") 
        
    if rect1[1][0] < rect2[0][0] or rect1[0][0] > rect2[1][0] or rect1[1][1] < rect2[0][1] or rect1[0][1] > rect2[1][1]:
        return False 
    
    return True