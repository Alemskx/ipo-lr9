from .CorrectRect import isCorrectRect

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        print("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        print("2й прямоугольник некоректный")
    
    x1, y1 = rect1[0]
    x2, y2 = rect1[1]
    x3, y3 = rect2[0]
    x4, y4 = rect2[1]
    
    return not (x3 >= x2 or x4 <= x1 or y3 >= y2 or y4 <= y1)



