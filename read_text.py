with open('referat.txt', 'r') as f:
    content = f.read()
    new_content = content.split(' ')
    print(len(new_content))