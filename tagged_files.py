import pdb
import shelve
import sys
import os

from lib.file_info import FileInfo

def open_db():
    db_path = sys.path[0]
    return shelve.open(f'{db_path}/tagged_files_info')

def init_file_info():
    file_name = sys.argv[2]
    file_path = os.path.abspath(file_name)
    return [file_name, file_path]    

def add_file_info():
    file_name, file_path = init_file_info()
    db_base = open_db()
  
    file_info = FileInfo(file_name, file_path)
  
    db_base[file_path] = file_info

    db_base.close()

def fetch_file_info():
    file_name, file_path = init_file_info()

    db_base = open_db()
  
    file_info = db_base[file_path]

    db_base.close()

    print(file_info.file_name)
    print(file_info.file_path)
    print(file_info.tags)

def add_tags_to_file():
    file_name, file_path = init_file_info()
    tags_list_str = sys.argv[3]

    db_base = open_db()
  
    file_info = db_base[file_path]
    file_info.add_tags(tags_list_str)
    db_base[file_path] = file_info

    db_base.close()

def clear_tags():
    file_name, file_path = init_file_info()
    db_base = open_db()
  
    file_info = db_base[file_path]
    file_info.clear_tags()
    db_base[file_path] = file_info

    db_base.close()

def tags_list():
    db_base = open_db()

    files_list = []
    for key in db_base.keys():
        files_list.append(db_base[key])

    tags_info_list = FileInfo.list_of_tags(files_list)

    tags_list = list(tags_info_list.keys())

    tags_outputs = map(lambda key: f'{key}({tags_info_list[key]})', tags_list)
    tags_cloud = ', '.join(tags_outputs)
    print(tags_cloud)

    db_base.close()

def find_by_tags():
    db_base = open_db()
    tags_string = sys.argv[2]
    tags_list = tags_string.split(',')

    for key in db_base.keys():
        file_info = db_base[key]
        #pdb.set_trace()
        if file_info.match_for_tags(tags_list):
            print(f'{key} => {file_info.file_name} => {file_info.tags}')

    db_base.close()


command = sys.argv[1]

match command:
    case 'add':
        add_file_info()
    case 'fetch':
        fetch_file_info()
    case 'tags':
        add_tags_to_file()
    case 'clear_tags':
        clear_tags()
    case 'tags_list':
        tags_list()
    case 'find':
        find_by_tags()

#pdb.set_trace()
