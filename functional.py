import os.path
import re
from datetime import datetime


def copy_file(file_name):
    if os.path.isfile(file_name):
        file_copy = f"{os.path.splitext(file_name)[0]}_copy{os.path.splitext(file_name)[1]}"
        with open(file_name, 'rb') as f:
            with open(file_copy, 'wb') as f_copy:
                for line in f:
                    f_copy.write(line)
    else:
        print('There is no such file!')


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('There is no such file!')


def count_files(dir_to_count):
    # Non-recursive
    counter = 0
    directory = os.path.normpath(dir_to_count)
    # print(dir)
    for item in os.listdir(directory):
        # print(item)
        if os.path.isfile(os.path.join(dir_to_count, item)):
            counter += 1
    print(f'There are currently: {counter} files in {directory}')
    return counter


def re_search(pattern, dir=os.getcwd()):
    cur_dir = dir
    result = list()
    print(f'We started! Pattern - {pattern} \n')
    for root, d, files in os.walk(cur_dir):
        # print(root, dir, files, sep='\n')
        for file in files:
            if re.search(pattern, file):
                result.append(os.path.join(root, file))
    for item in result:
        print(item + '\n')
    return result


def date_file(path, recursive=False):
    if os.path.isfile(path):
        date_of_creation = os.stat(path).st_ctime
        name = os.path.split(path)[1]
        readable_date = datetime.fromtimestamp(date_of_creation).strftime('%Y_%m_%d')
        new_name = f"{readable_date}_{name}"
        new_dir = os.path.join(os.path.split(path)[0], new_name)
        os.rename(path, new_dir)
    if os.path.isdir(path) and recursive == False:
        dir = os.listdir(path)
        for item in dir:
            #print(os.path.join(path, item))
            #print(os.path.isfile(os.path.join(path, item)))
            if os.path.isfile(os.path.join(path, item)):
                date_of_creation = os.stat(path).st_ctime
                readable_date = datetime.fromtimestamp(date_of_creation).strftime('%Y_%m_%d')
                new_name = f"{readable_date}_{item}"
                os.rename(os.path.join(path, item), os.path.join(path, new_name))

    if os.path.isdir(path) and recursive == True:
        for root, dir, item in os.walk(path):
            for i in item:
                date_of_creation = os.stat(os.path.join(root, i)).st_ctime
                readable_date = datetime.fromtimestamp(date_of_creation).strftime('%Y_%m_%d')
                new_name = f"{readable_date}_{i}"
                os.rename(os.path.join(root, i), os.path.join(root, new_name))
