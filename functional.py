import os.path


def copy_file(file_name):
    if os.path.isfile(file_name):
        file_copy = f"{os.path.splitext(file_name)[0]}_copy{os.path.splitext(file_name)[1]}"
        with open(file_name, 'rb') as f:
            with open(file_copy, 'wb') as f_copy:
                for line in f:
                    f_copy.write(line)
        #return file_copy
    else:
        print('There is no file like this!')

def delete_file(file_name):
    os.remove(file_name)

def count_files(dir_to_count):
    counter = 0
    print(f'started curdir = {dir_to_count.name}')
    if(os.path.exists(dir_to_count.name)):
        for root, dir, file in os.walk(dir_to_count.name):
            print(root)
            print(dir)
            print(file)
            for file in file:
                print(file)
                counter += 1
    else:
        raise NotADirectoryError ("No dir!")
    return counter