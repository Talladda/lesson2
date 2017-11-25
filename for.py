<<<<<<< HEAD
student_assessment = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, 
    {'school_class': '5a', 'scores': [5, 4, 2, 3, 3]}, 
    {'school_class':  '3b', 'scores': [3, 5, 5, 2, 4]}
]
variable = list()
def class_arifm():
    for item in student_assessment:
        variable.append((sum(item['scores']) / len(item['scores'])))
    print(variable)
def school_arifm():
    class_arifm()
    print(sum(variable) / len(variable))
=======
student_assessment = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, 
    {'school_class': '5a', 'scores': [5, 4, 2, 3, 3]}, 
    {'school_class':  '3b', 'scores': [3, 5, 5, 2, 4]}
]
variable = list()
def class_arifm():
    for item in student_assessment:
        variable.append((sum(item['scores']) / len(item['scores'])))
    print(variable)
def school_arifm():
    class_arifm()
    print(sum(variable) / len(variable))
>>>>>>> 81ab7f4369cf5ae28a34288571973b0f51165406
school_arifm()