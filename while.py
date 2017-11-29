<<<<<<< HEAD
#names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#while names.pop() != "Валера":
#    if len(names) == 0:
#        print("Валера отсутствует в списке")
#        break
#if len(names) != 0:
#    print("Валера нашелся")
#print(names)

#person = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#def find_person(name):
#    index = 0
#    while index < len(person):
#        if person[index] != name:
#            index = index + 1
#        else:
#            return print(person[index] + ' - ' + str(index))
#    return print("Указанного имени в списке нет")
#find_person(input('Введите имя: '))

def get_answer(message):
    while message != "Пока":
        message = input("Сейчас ответить не могу. Хочешь что-то еще спросить? ")
    return 0
def ask_user(message):
    while message != "Хорошо":
        message = input("Как дела? ")
    get_answer(input("У меня тоже все хорошо. Хочешь что-то спросить? "))
=======
#names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#while names.pop() != "Валера":
#    if len(names) == 0:
#        print("Валера отсутствует в списке")
#        break
#if len(names) != 0:
#    print("Валера нашелся")
#print(names)

#person = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
#def find_person(name):
#    index = 0
#    while index < len(person):
#        if person[index] != name:
#            index = index + 1
#        else:
#            return print(person[index] + ' - ' + str(index))
#    return print("Указанного имени в списке нет")
#find_person(input('Введите имя: '))

def get_answer(message):
    while message != "Пока":
        message = input("Сейчас ответить не могу. Хочешь что-то еще спросить? ")
    return 0
def ask_user(message):
    while message != "Хорошо":
        message = input("Как дела? ")
    get_answer(input("У меня тоже все хорошо. Хочешь что-то спросить? "))
>>>>>>> 81ab7f4369cf5ae28a34288571973b0f51165406
ask_user(input("Как дела? "))