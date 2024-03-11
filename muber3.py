# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]


# Здесь напишите ваше генераторное выражение.
numbers_generation = (number**2 for number in numbers if number % 3 == 0)

total_squares = sum(numbers_generation)

print(total_squares)