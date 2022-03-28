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

#pdb.set_trace()
