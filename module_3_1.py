calls = 0
#Функция count_calls подсчитывающая вызовы остальных функций
def count_calls():
    global calls
    calls += 1
    return calls


#Функция string_info принимает аргумент - строку и возвращает кортеж из:
#длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_


#Функция is_contains принимает: строку и список, и возвращает True,
#если строка находится в этом списке, False - если отсутствует
def is_contains(string, list_to_search):
    string = string.lower()
    for element in list_to_search:
        number = list_to_search.index(element)
        if type(element) is str:
            list_to_search[number] = element.lower()
        else:
            continue
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(string_info('single5'))
print(is_contains('sun', ['SUnlight', '34', 'sun3', 78]))
print(calls)
