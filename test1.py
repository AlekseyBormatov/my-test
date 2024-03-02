# Без аннотации: объявили переменную, 
# а Python сам определил, какой в ней тип данных.
birth_year = 1971

# С аннотацией: объявили переменную и указали, 
# что это переменная только для целых чисел.
birth_year: int = 1971

# Общий синтаксис аннотирования переменных:

# Переменная var_for_bool аннотирована как булева, но в неё передана строка.
var_for_bool: bool = 'Чистая правда, клянусь!'

print(type(var_for_bool))