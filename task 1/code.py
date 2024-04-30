import re

path = r'C:\Users\Руслан\Documents\GitHub\goit-pycore-hw-04\task 1\text.txt'

def total_salary(path):
    try:
        with open(path, 'r+') as file:            
            file_content = file.read()            
            file.seek(0)
            numbers = []

            line_count = 0 
            for line in file:  
                result = line.split(',') 
                numbers.append(result[1])        
                line_count += 1 
            
            sum_salary = 0
            for num in numbers:
                sum_salary = sum_salary + int(num)
            average_salary = sum_salary // line_count
            result = (sum_salary, average_salary)

            return result
    except Exception as e:
        print("error", e)

print(total_salary(path))