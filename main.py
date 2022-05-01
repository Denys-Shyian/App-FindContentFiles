import os

DIRECTORY = r'A:\Проекты\Разработки\Python\FindContentFiles\Test'
FIND_STRING = 'обеспече'
COUNT_ADDING_SYMBOLS = 10


def find(find_directory, find_string):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            find_string_in_file(os.path.join(root, name), find_string)


def find_string_in_file(file, find_string):
    f = open(file, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    index = content.find(find_string)
    if index != -1:
        print_find_info(file, content, find_string)


def print_find_info(file, content, find_string):
    index = content.find(find_string)
    start_index = index - COUNT_ADDING_SYMBOLS if index >= COUNT_ADDING_SYMBOLS else 0
    end_index = index + len(find_string) + COUNT_ADDING_SYMBOLS
    content = content[start_index:end_index]
    content = content.replace(find_string, "\x1b[36;1m" + find_string + "\x1b[0m")
    print(f'{file}:\n{content}')


if __name__ == '__main__':
    find(DIRECTORY, FIND_STRING)
