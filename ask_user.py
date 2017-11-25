answer = {
    "привет": "И тебе привет!", 
    "как дела": "Лучше всех", 
    "что делаешь": "Думаю"
}
question = input()
question = question.lower()
def main(question, answer):
    def get_answer(question, answer): 
            return answer.get(question)
    if question in answer.keys():
        get_answer(question, answer)
    elif question == 'пока':
        return 0
    elif question.isdigit():
            try:
                print(answer[question].keys)
            except (ZeroDivisionError, KeyboardInterrupt, Exception):
                print("Было введено неверное значение. Пока")
                return 1
    else:
        return 1
    print(get_answer(question, answer))
main(question, answer)