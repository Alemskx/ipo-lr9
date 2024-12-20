from collision.CorrectRect import isCorrectRect
from collision.CollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect 
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect 
# Примеры 
print("Функция 1")
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  #True

print("Функция 2")
print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))  #True

print("Функция 3")
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))  #положительное число

print("Функция 4")
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")
