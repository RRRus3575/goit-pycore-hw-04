

def get_cats_info(path):
    try:
        with open(path, 'r+') as file:            
            file_content = file.read()            
            file.seek(0)
            cats_list = []

            for line in file:
                result = line.split(',')
                cat_dict = {
                    'id': result[0],
                    'name': result[1],
                    'age': result[2]
                }
                cats_list.append(cat_dict)

            return cats_list


    except Exception as e:
        print('error', e)



