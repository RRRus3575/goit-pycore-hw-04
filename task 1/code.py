import re

path = 'text.txt'

def total_salary(path):
    try:
        with open(path, 'r+') as file:
            print(file)
            file_content = file.readline()
            print(file_content)
            file.seek(0)
            numbers = re.findall(r'\d+', file_content)
            print(numbers)
    except Exception as e:
        print("Ошибка при чтении файла:", e)