from random import choice, uniform


def test_function_1():
    """Возвращает случайное число типа float в диапазоне от -10 до 10,
    например -4.3897268052813265.
    """
    return uniform(-10, 10)

x = test_function_1()
#y = 5.2234
#print(test_function_1())

print(x)
#if isinstance(x, float):
    #print('Как это может быть флоат?')

print(type(x))
#print(y)
#print(type(y))