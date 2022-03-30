import pdb

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

    def match_for_tags(self, tags_list):
        matched_tags = set(tags_list).intersection(self.tags)
        return len(matched_tags) == len(tags_list)

    @classmethod
    def list_of_tags(cls, list_of_files):
        tags_list = {}
        for file_info in list_of_files:
            for tag in file_info.tags:
                tags_list[tag] = tags_list.get(tag, 0) + 1

        return tags_list