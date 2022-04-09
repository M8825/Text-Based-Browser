import argparse
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

parser = argparse.ArgumentParser()
parser.add_argument('dir_name', type=str)

args = parser.parse_args()
dir_path = args.dir_name

if not os.access(dir_path, os.F_OK):
    os.mkdir(dir_path)


def file_name(f_name):
    """ Format full path to file

    :param f_name: Name of the file
    :return: Full path
    """
    name = f_name[:-4] if '.' in f_name else f_name  # Assign without '.com' if it's present

    return f'{dir_path}/{name}'


def save_file(f_name, c):
    path = file_name(f_name)
    with open(path, 'w', encoding='utf-8') as f_article:
        f_article.writelines(c)
        f_article.close()


def file_exists(f_name):
    path = file_name(f_name)
    return os.access(path, os.F_OK)


while True:
    url = input()
    if url == 'exit':
        break

    if '.' not in url and file_exists(url):  # If only valid filename have been passed and file exists.
        f_path = file_name(url)
        with open(f_path, 'r', encoding='utf-8') as file:
            print(file.read())
            file.close()
            continue

    if '.' not in url:  # If input is not proper URL
        print('Error: Incorrect URL')
        continue

    if url == 'bloomberg.com':
        content = bloomberg_com
        print(bloomberg_com)
    elif url == 'nytimes.com':
        content = nytimes_com
        print(nytimes_com)
    else:
        print('Error: Incorrect URL')
        continue

    save_file(url, content)
