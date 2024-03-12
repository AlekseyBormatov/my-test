people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda a :print('Здравствуй, ' + a + '!') if 'С' in a else print('Привет, ' + a + '!'), people)