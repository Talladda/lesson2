<<<<<<< HEAD
def fun(strs, strings):
    if strs == strings:
        return '1'
    elif len(strs) > len(strings) and strings != 'learn':
        return '2'
    elif strings == 'learn':
        return '3'
=======
def fun(strs, strings):
    if strs == strings:
        return '1'
    elif len(strs) > len(strings) and strings != 'learn':
        return '2'
    elif strings == 'learn':
        return '3'
>>>>>>> 81ab7f4369cf5ae28a34288571973b0f51165406
print(fun(input('Введите первую строку: '), input('Введите вторую строку: ')))