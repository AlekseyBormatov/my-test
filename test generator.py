# Создать функцию-генератор.
def short_sequence():
    num = 1
    while num < 5:
    # Сгенерировать значение через yield.
        yield num
        num += 1

# Здесь функция-генератор возвращает итератор.
step = short_sequence()
print(step.__next__())
print(step.__next__())
print(step.__next__())


# Обратиться к методу __next__() итератора
# и получить первое значение последовательности.
#print(step.__next__())

# Ещё раз обратиться к методу __next__()
# и получить второе значение последовательности.
#print(step.__next__())