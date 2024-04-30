
path = r'C:\Users\Руслан\Documents\GitHub\goit-pycore-hw-04\task 2\file.txt'

def get_cats_info(path):
    try:
        with open(path, 'r+') as file:                        
            file.seek(0)
            cats_list = []

            for line in file:
                result = line.split(',')
                cat_dict = {
                    'id': result[0],
                    'name': result[1],
                    'age': result[2].rstrip('\n')
                }
                cats_list.append(cat_dict)

            return cats_list


    except Exception as e:
        print('error', e)



print(get_cats_info(path))