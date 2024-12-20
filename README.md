## Задание 1

Создайте пакет `collision` в вашем репозитории.

## Задание 2

Создайте функцию `isCorrectRect`  которая принимает в качестве аргументов список из двух кортежей, каждый кортеж состоит из координат точки(*двух чисел, `x` и `y`*): 

1. первый — координат левого нижнего угла прямоугольника 
2. второй — координат верхнего правого угла прямоугольника 

Функция возвращает `True` или `False` в зависимости от того  корректно ли введены результаты.

Как пример:

```python
isCorrectRect([(-3.4, 1),(9.2, 10)]) # Вернет True

isCorrectRect([(-7, 9),(3, 6)]) # Вернет False
```

<aside>
🚨

После того как задание сделано создать коммит с комментарием “Task 2 complete”

</aside>

## Задание 3

Создайте функцию `isCollisionRect` которая принимает в качестве аргументов списков из двух списков, которые в свою очередь состоит из двух кортежей, каждый кортеж состоит из координат точки(*двух чисел, `x` и `y`*): 

1. первый — координат левого нижнего угла прямоугольника 
2. второй — координат верхнего правого угла прямоугольника 

Функция возвращает `True` или `False` в зависимости от того пересекаются ли прямоугольники или нет.

Если в функцию передан некорректный прямоугольник функция вызывает ошибку `RectCorrectError` c комментарием “`1й прямоугольник некоректный`”. Про вызов ошибок можно почитать в [теоретической части](https://www.notion.so/9-1359f5faa7fd80ce9d66e1dac8566775?pvs=21).

Как пример:

```python
isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]) # Вернет True

isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]) # Вернет False

isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]) # Вызовет ошибку
```

<aside>
🚨

После того как задание сделано создать коммит с комментарием “Task 3 complete”

</aside>

## Задание 4

Создайте функцию `intersectionAreaRect` которая принимает в качестве аргументов два списка, каждый из которых состоит из двух кортежей. Каждый кортеж содержит координаты точки (два числа, `x` и `y`):

1. первый — координаты левого нижнего угла прямоугольника
2. второй — координаты верхнего правого угла прямоугольника

Функция должна возвращать площадь пересечения двух прямоугольников. Если прямоугольники не пересекаются, функция должна вернуть 0.

Если в функцию передан некорректный прямоугольник, функция должна вызвать ошибку `ValueError` с соответствующим комментарием.

Пример использования:

```python
intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]) # Вернет некоторое положительное число

intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]) # Вернет 0

intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]) # Вызовет ошибку
```

<aside>
🚨

После того как задание сделано создать коммит с комментарием "Task 4 complete"

</aside>

## Задание 5

Создайте функцию `intersectionAreaMultiRect`, которая принимает в качестве аргумента список списков. Каждый внутренний список состоит из двух кортежей, представляющих координаты прямоугольника:

1. первый кортеж — координаты левого нижнего угла прямоугольника
2. второй кортеж — координаты верхнего правого угла прямоугольника

Функция должна возвращать общую площадь пересечения всех переданных прямоугольников, учитывая только уникальные области пересечения без повторений.

Если в функцию передан некорректный прямоугольник, функция должна вызвать ошибку `RectCorrectError` с соответствующим комментарием.

Пример использования:

```python
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")

# Некорректный прямоугольник
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]  # Некорректный прямоугольник
]
intersectionAreaMultiRect(incorrect_rectangles)  # Вызовет ошибку
```

Функция должна эффективно обрабатывать случаи с любым количеством прямоугольников и учитывать все возможные пересечения между ними.

<aside>
🚨

После того как задание сделано создать коммит с комментарием “Task 5 complete”

</aside>

## Задание 6

Импортировать все функции из пакета в файл [`main.py`](http://main.py) , и привести примеры использования каждой из них.
