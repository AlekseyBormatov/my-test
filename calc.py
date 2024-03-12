people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda a : print('Привет', a), people)
# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
#say_to_all(lambda b : f'До завтра, {b}!', people)
say_to_all(lambda b : print('До завтра', b), people)

#say_to_all(print, people)

#a = 'Семен' 
#print((lambda a : f'Привет, {a}!') ('Семен'))