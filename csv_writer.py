import csv

answer = [
    {"answ": "How are you?", "ques": "Fine"}, 
    {"answ": "What's your name", "ques": "Tom"}, 
    {"answ": "What are you doing", "ques": "I'm reading"}
]

with open('export.csv', 'w', encoding='utf-8') as f:
    field = ['answ', 'ques']
    writer = csv.DictWriter(f, field, delimiter=';')
    writer.writeheader()
    for row in answer:
        writer.writerow(row)