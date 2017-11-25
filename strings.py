def fun(strs, strings):
    if strs == strings:
        return '1'
    elif len(strs) > len(strings) and strings != 'learn':
        return '2'
    elif strings == 'learn':
        return '3'
print(fun(input('Введите первую строку: '), input('Введите вторую строку: ')))