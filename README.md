# Tagged Files
Command Line application for tagging files

## System Requirements
  * Python >= 3.10

## Usage
To add a file to db:
```bash
$ python3.10 tagged_files.py add /home/fat_shinobi/stuff/litra/ruby/rails/Security.on.Rails.pdf
```

To set tags for the file:
```bash
$ python3.10 tagged_files.py tags /home/fat_shinobi/stuff/litra/ruby/rails/Security.on.Rails.pdf books,security,rails,ruby,programming
```

To show file info:
```bash
$ python3.10 tagged_files.py fetch /home/fat_shinobi/stuff/litra/ruby/rails/Security.on.Rails.pdf
Security.on.Rails.pdf
/home/fat_shinobi/stuff/litra/ruby/rails/Security.on.Rails.pdf
['books', 'security', 'rails', 'ruby', 'programming']
```

To show tags:
```bash
$ python3.10 tagged_files.py tags_list
books(3), programming(2), python(1), ruby(2), security(1), rails(1)
```

To find files by tag:
```bash
$ python3.10 tagged_files.py find books
/home/fat_shinobi/stuff/litra/python/codding/Дауни А. - Основы Python - 2021.pdf => Дауни А. - Основы Python - 2021.pdf => ['books', 'programming', 'python']
/home/fat_shinobi/stuff/litra/ruby/Shopyfy.pdf => Shopyfy.pdf => ['books', 'ruby']
/home/fat_shinobi/stuff/litra/ruby/rails/Security.on.Rails.pdf => Security.on.Rails.pdf => ['books', 'security', 'rails', 'ruby', 'programming']
```