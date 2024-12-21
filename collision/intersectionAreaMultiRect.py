from .isCorrectRect import isCorrectRect

class RectCorrectError(Exception):
    pass

def intersectionAreaMultiRect(rects_coords):
    unique_coords = []

    for num_of_rect, rect in enumerate(rects_coords, start=1):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Некорректный {num_of_rect} прямоугольник")
        
        if rect not in unique_coords:
            unique_coords.append(rect)
    
    total_square = 0
    kol_uniq_coords = len(unique_coords)

    for i in range(kol_uniq_coords):
        for j in range(i + 1, kol_uniq_coords):
            (x_left1, y_left1), (x_right2,y_right2) = unique_coords[i]
            (x_left3, y_left3), (x_right4,y_right4) = unique_coords[j]

            if x_left1 > x_right4 or y_left1 > y_right4 or x_right2 < x_left3 or y_right2 < y_left3:
                continue

            xCross_left = max(x_left1, x_left3)
            yCross_bottom = max(y_left1, y_left3)
            xCross_right = min(x_right2, x_right4)
            yCross_top = min(y_right2, y_right4)

            crossWidth = xCross_right - xCross_left
            crossHeight = yCross_top - yCross_bottom

            if crossWidth > 0 and crossHeight > 0:  
                total_square += crossWidth * crossHeight

    return total_square
  
