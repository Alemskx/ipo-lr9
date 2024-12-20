from .CorrectRect import isCorrectRect

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некоректный")
    #Определение координат пересечения
    x1 = max(rect1[0][0], rect2[0][0])
    y1 = max(rect1[0][1], rect2[0][1])
    x2 = min(rect1[1][0], rect2[1][0])
    y2 = min(rect1[1][1], rect2[1][1])
    #Возвращщение площади
    if x1 >= x2 or y1 >= y2:
        return 0
    return (x2 - x1) * (y2 - y1)

