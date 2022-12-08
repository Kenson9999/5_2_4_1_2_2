import os

def get_directory_list(data):
    content = list()
    for item in os.scandir(data):
        if os.path.isdir(item):
            content.append(item.name)
    return content
def get_file_list(data):
    content = list()
    for item in os.scandir(data):
        if os.path.isfile(item):
            content.append(item.name)
    return content