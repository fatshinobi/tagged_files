class FileInfo:
    def __init__(self, filename, filepath):
        self.file_name = filename
        self.file_path = filepath
        self.tags = []

    def add_tags(self, tags_list_str):
        tags_list = tags_list_str.split(',')
        self.tags += tags_list

    def clear_tags(self):
        self.tags = []