import os.path


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
