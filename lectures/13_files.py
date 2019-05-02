# **********************************************Files**********************************************

# In this lecture we will learn how to work with file system (getting files and their attributes
# in directory, creating new directories and etc.), how to work with files (open file, read file
# content, edit file content, delete file and etc.). Lecture will introduce also different file
# types, which are supported by pure Python (txt, json, csv and etc.)


# *************************************Part 1: File system*****************************************

# Working with files and interacting with the file system are important for many different reasons.
# The simplest cases may involve only reading or writing files, but sometimes more complex tasks
# are at hand. Maybe you need to list all files in a directory of a given type, find the parent
# directory of a given file, or create a unique file name that does not already exist.
#
# Traditionally, Python has represented file paths using regular text strings. With support from
# the os.path standard library, this has been adequate although a bit cumbersome. However,
# since paths are not strings, important functionality is spread all around the standard library,
# including libraries like os, glob, and shutil.

# With paths represented by strings, it is possible, but usually a bad idea, to use regular string
# methods. For instance, instead of joining two paths with + like regular strings, you should use
# os.path.join(), which joins paths using the correct path separator on the operating system.
# Recall that Windows uses \ while Mac and Linux use / as a separator. This difference can lead to
# hard-to-spot errors, such as our first example in the introduction working for only Windows
# paths.

# In Python 3.3 or lower version paths mainly were handled using os.path module, which mainly
# treated them as strings. The pathlib module was introduced in Python 3.4 (PEP 428) to deal with
# these challenges. It gathers the necessary functionality in one place and makes it available
# through methods and properties on an easy-to-use Path object.


import os
import shutil
from pathlib import Path

# We will introduce pathlib module and parallel will discuss also os.path module.


# Get current directory

# shows the current directory from where the code is run
print(Path.cwd())
print(os.getcwd())

# Getting a Directory listing (everything which is in directory)
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures'

files = Path(directory_path)
for x in files.iterdir():  # Returns an iterator of all the objects in a directory
    print(x)
    print(type(x))  # This will be again Path object (PosixPath or WindowsPath)

files = os.listdir(directory_path)  # Returns a list of all files and folders in a directory
for x in files:
    print(x)
    print(type(x))  # This will be str

# Listing only Files in a Directory
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures'

files = Path(directory_path)
for x in files.iterdir():
    if x.is_file():
        print(x)

files = os.listdir(directory_path)
for x in files:
    full_path = os.path.join(directory_path, x)
    if os.path.isfile(full_path):
        print(full_path)

# Listing only Subdirectories in a Directory
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures'

files = Path(directory_path)
for x in files.iterdir():
    if x.is_dir():
        print(x)

files = os.listdir(directory_path)
for x in files:
    full_path = os.path.join(directory_path, x)
    if os.path.isdir(full_path):
        print(full_path)

# Getting File Attributes
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures'

files = Path(directory_path)
for x in files.iterdir():
    if x.is_file():
        print(x)
        print(x.stat())

files = os.listdir(directory_path)
for x in files:
    full_path = os.path.join(directory_path, x)
    if os.path.isfile(full_path):
        print(full_path)
        print(os.stat(full_path))

# Note
# pathlib.Path() retrieve a directory listing with file attributes combined. This is more efficient
# than using os.listdir() to list files and then getting file attribute information for each file.

# Creating a Single Directory
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir'

p = Path(directory_path)
p.mkdir()

# if we call again, we will have en error: FileExistsError
try:
    p.mkdir()
except FileExistsError as e:
    print(e)

# in order to avoid such error we can use exist_ok keyword argument
p.mkdir(exist_ok=True)

# the same with os
try:
    os.mkdir(directory_path)  # this do not have exist_ok keyword argument
except FileExistsError as e:
    print(e)

# Deleting Files and Directories

# To remove single file we can use pathlib.Path.unlink() or os.remove().
# Both are used for deleting only files and do not delete directories.

# lets create a single txt file and try to remove it
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir'
file_path = os.path.join(directory_path, 'new_file.txt')

with open(file_path, 'w') as infile:
    infile.write('hello')

# now lets remove it with Path.unlink()
p = Path(file_path)
if p.is_file():  # we have to ensure that this is file
    p.unlink()

with open(file_path, 'w') as infile:
    infile.write('hello')

# now lets remove it with os.remove()
if os.path.isfile(file_path):
    os.remove(file_path)

# if we try to remove a directory with p.unlink() or os.remove() we will have an error
try:
    p = Path(directory_path)
    p.unlink()
except OSError as e:
    print(e)

try:
    os.remove(directory_path)
except OSError as e:
    print(e)

# Now lets delete a directory itself.
# There are 2 possible options: directory is empty and not empty.

# If the directory is empty, we can use os.rmdir() or pathlib.Path.rmdir().
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir'

p = Path(directory_path)
if p.is_dir():
    p.rmdir()

# creating again, for deleting os.rmdir()
p.mkdir()
if os.path.isdir(directory_path):
    os.rmdir(directory_path)

# If the directory is not empty, we should use shutil.rmtree(). It will delete non-empty
# directories and entire directory trees.
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir'
p = Path(directory_path)
p.mkdir(exist_ok=True)

file_path = os.path.join(directory_path, 'new_file.txt')
with open(file_path, 'w') as infile:
    infile.write('hello')

shutil.rmtree(directory_path, ignore_errors=True)

# Creating Multiple Directories
# For creating multiple directories (aka nested directories) we can use
# pathlib.Path.mkdir(parents=True) or os.makedirs()

directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir/good/directory'

p = Path(directory_path)
p.mkdir(parents=True, exist_ok=True)

# lets delete it and try with os.makedirs()
shutil.rmtree('/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir')

os.makedirs(directory_path, exist_ok=True)
shutil.rmtree('/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir')

# Copying, Moving, and Renaming Files and Directories

# for copping src single file to destination:
# shutil.copy(src, dst)

# for copping an entire directory and everything contained in it:
# shutil.copytree(src, dest)

# for moving a file or directory to another location:
# shutil.move(src, dst)

# for renaming files and directories:
# os.rename(src, dst)


# Filename Pattern Matching

# After getting a list of files in a directory using one of the methods above, you will most
# probably want to search for files that match a particular pattern.

directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/data'
files = Path(directory_path)

for p in files.iterdir():
    if p.is_file():
        print()
        print(f'type of path: {type(p)}')
        print(f'path object: {p}')
        print(f'file name: {p.name}')  # the file name without any directory
        print(f'file stem {p.stem}')  # the file name without the suffix (extension)
        print(f'file extension {p.suffix}')  # the file extension
        print(f'file directory {p.parent}')  # the directory containing the file
        print(f'file anchor {p.anchor}')  # the part of the path before the directories

# for example we want only .txt files

# using suffix == extension
txt_files = [p for p in files.iterdir() if p.is_file() and p.suffix == '.txt']
print(f'txt_files: {txt_files}')

# using str.endswith() method
txt_files = [p for p in files.iterdir() if p.is_file() and p.name.endswith('.txt')]
print(f'txt_files: {txt_files}')

# using fnmatch
from fnmatch import fnmatch

txt_files = [p for p in files.iterdir() if p.is_file() and fnmatch(p.name, '*.txt')]
print(f'txt_files: {txt_files}')

# more complicated example
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/lectures'
files = Path(directory_path)

lectures = [p for p in files.iterdir()
            if p.is_file() and fnmatch(p.name, '*_data_structures*.py')]
print(f'data_structure related lectures: \n{lectures}')

# using Path.glob()
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/data'
files = Path(directory_path)

txt_files = [p for p in files.glob('*.t*')]
print(f'file types that start with the letter t: {txt_files}')

# **************************************Part 2: File I/O*******************************************
#
# File is a named location on disk to store related information. It is used to permanently store
# data in a non-volatile memory (e.g. hard disk).
#
# Since, random access memory (RAM) is volatile which loses its data when computer is turned off,
# we use files for future use of the data.
#
# When we want to read from or write to a file we need to open it first. When we are done, it needs
# to be closed, so that resources that are tied with the file are freed.
#
# There are two separate types of files that Python handles: binary and text files. Knowing the
# difference between the two is important because of how they are handled.
#
# Most files that you use during your normal computer use are actually binary files, not text.
# That’s right, that Microsoft Word .doc file is actually a binary file, even if it just has text
# in it.
#
# Binary files examples:
# Image files including .jpg, .png, .bmp, .gif, etc.
# Database files including .mdb, .frm, and .sqlite
# Documents including .doc, .xls, .pdf, and others.
#
# That’s because these files all have requirements for special handling and require a specific type
# of software to open it. For example, you need Excel to open an .xls file, and a database program
# to open a .sqlite file.
#
# A text file on the other hand, has no specific encoding and can be opened by a standard text
# editor without any special handling. Still, every text file must adhere to a set of rules.
#
# Text files have to be readable as is. They can (and often do) contain a lot of special encoding,
# especially in HTML or other markup languages, but you’ll still be able to tell what it says
# Data in a text file is organized by lines. In most cases, each line is a distinct element,
# whether it’s a line of instruction or a command.
#
# When working in Python, you don’t have to worry about importing any specific external libraries
# to work with files. Python comes with “batteries included” and the file I/O tools and utilities
# are a built-in part of the core language.
#
# In Python, a file operation takes place in the following order:
# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file
#
# Opening files
#
# For opening file, we just use built in open function:
# file_object = open(file path, mode, encoding)

# The mode in the open function tells Python what you want to do with the file.
# There are multiple modes that you can specify when dealing with text files.

# 'w' –  Write Mode: This mode is used when the file needs to be altered and information changed or
#        added. Keep in mind that this erases the existing file to create a new one.
#        File pointer is placed at the beginning of the file.
# 'r' –  Read Mode: This mode is used when the information in the file is only meant to be read and
#        not changed in any way. File pointer is placed at the beginning of the file.
# 'a' –  Append Mode: This mode adds information to the end of the file automatically. File pointer
#        is placed at the end of the file.
# 'r+' – Read/Write Mode: This is used when you will be making changes to the file and reading
#        information from it. The file pointer is placed at the beginning of the file.
# 'a+' – Append and Read Mode: A file is opened to allow data to be added to the end of the file
#        and lets your program read information as well. File pointer is placed at the end of the
#        file.
# 'x' –  Exclusive Creation Mode: This mode is used exclusively to create a file. If a file of the
#        same name already exists, the function call will fail.
#
# When you are using binary files, you will use the same mode specifiers. However, you add a b to
# the end. So a write mode specifier for a binary file is 'wb'. The others are 'rb', 'ab', 'r+b',
# and 'a+b' respectively.

# The default encoding is platform dependent. In windows, it is 'cp1252' but 'utf-8' in Linux.

file_object = open('ACA_2019_python_lectures/data/a.txt', 'r+')
print(file_object)
print(type(file_object))

# When we are done with operations to the file, we need to properly close the file.
# Closing a file will free up the resources that were tied with the file and is done using
# Python close() method.
file_object.close()
print(file_object.closed)

# This method is not entirely safe. If an exception occurs when we are performing some operation
# with the file, the code exits without closing the file.
#
# The best way to do this is using the "with" statement. This ensures that the file is closed when
# the block inside with is exited.
# We don't need to explicitly call the close() method. It is done internally.
with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    # perform file operations
    print('file operations is finished')
    print(f'file name is: {file_object.name}')
    print(f'file encoding is: {file_object.encoding}')
    print(f'file is closed: {file_object.closed}')

print(f'file is closed: {file_object.closed}')

# Once you’ve successfully opened a file, you can use built-in methods to deal with the new file
# object. You can read data from it, or write new data to it.


# Reading Data From a File

# read(size) method

# We can read data using file_object.read(size) method. By default, this method will read the
# entire file and print it out to the console as either a string (in text mode) or as byte objects
# (in binary mode).

# You have to be careful when using the default size, however. If the file you’re reading is larger
# than your available memory, you won’t be able to access the entire file all at once. In a case
# like this, you need to use the size parameter to break it up into chunks your memory can handle.
# The size parameter tells the read method how many bytes into the file to return to the display.
with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    file_content = file_object.read(-1)
    print(f'\nthe file full content is: \n{file_content}')

with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    file_content = file_object.read(6)
    print(f'\nthe file chunk content is: \n{file_content}')
    print(len(file_content))
    print(type(file_content))
    print(list(file_content))
    # As you can see, the read operation only read the data in the file up to position 6,
    # which is what we passed to the read() call above. That way you can limit how much data is
    # read from a file in one go.

    # If you read from the same file object again, it will continue reading data where you left
    # off. That way you can process a large file in several smaller “chunks.”
    file_content = file_object.read(6)
    print(f'\nthe file chunk content is: \n{file_content}')
    print(len(file_content))
    print(type(file_content))
    print(list(file_content))

    file_content = file_object.read(6)
    print(f'\nthe file chunk content is: \n{file_content}')
    print(len(file_content))
    print(type(file_content))
    print(list(file_content))
    # ....

# readline(limit) method

# We can also parse data in a file by reading it line by line. This can let you scan an entire
# file line by line, advancing only when you want to, or let you see a specific line.


with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    line = file_object.readline()  # first line
    print(f'\nthe file line content is: \n{line}')
    print(len(line))
    print(type(line))
    print(list(line))

    line = file_object.readline(3)  # second line first 3 chars
    print(f'\nthe file line content is: \n{line}')
    print(len(line))
    print(type(line))
    print(list(line))

    line = file_object.readline()  # second line rest chars
    print(f'\nthe file line content is: \n{line}')
    print(len(line))
    print(type(line))
    print(list(line))

    line = file_object.readline()  # third line
    print(f'\nthe file line content is: \n{line}')
    print(len(line))
    print(type(line))
    print(list(line))

# As you can see, this reads the whole file into memory and splits it up into several lines. This
# only works with text files however. A binary file is just a blob of data—it doesn’t really have a
# concept of what a single line is.

# readlines() method

# A similar method is the fileobject.readlines() call (notice the plural), which returns every
# line in a list format.

with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    lines = file_object.readlines()  # all lines list
    print(f'\nthe file line content is: \n{lines}')
    print(len(lines))
    print(type(lines))

# Processing an Entire Text File Line-By-Line

# The easiest way to process an entire text file line-by-line in Python is by using a simple loop:

lines = []
with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    for line in file_object:
        print(line)
        print(type(line))
        print(len(line))
        lines.append(line.replace('\n', ''))
print(" ***** ".join(lines))


# In case our file is huge and we can get memory errors, we can use lines generator function:
def file_lines_generator(file_path: str):
    with open(file_path, 'r') as file_object:
        for line in file_object:
            yield line


generator_obj = file_lines_generator('ACA_2019_python_lectures/data/a.txt')
print(type(generator_obj))

for x in generator_obj:
    print(x)

# Writing to a File With Python Using write()


# Remember that when you create a new file object, Python will create the file if one doesn’t
# already exist. When creating a file for the first time, you should either use the a+ or w+ modes.

# Often it’s preferable to use the a+ mode because the data will default to be added to the end of
# the file. Using w+ will clear out any existing data in the file and give you a “blank slate” to
# start from.


values_to_write = [10, 'good', 'day', 3.5]
with open('ACA_2019_python_lectures/data/a.txt', 'a+') as file_object:
    for x in values_to_write:
        file_object.write('\n' + str(x) + '\n')

# We can write list of lines with writelines method:
values_to_write = [1, 2, 3]
with open('ACA_2019_python_lectures/data/a.txt', 'a+') as file_object:
    values_to_write = ['\n' + str(x) + '\n' for x in values_to_write]
    file_object.writelines(values_to_write)

# File Seeks: Moving the Read/Write Pointer

# Remember that when you write using the a+ mode, your file pointer is always going to be at the
# end of the file. If you want to move the pointer, you should use the
# fileobject.seek(offset, from_what) method. In this method, you put the pointer at a specific
# spot. The offset is the number of characters from the from_what parameter. The
# from_what parameter has three possible values:
#
# 0 – indicates the beginning of the file
# 1 – indicates the current pointer position
# 2 – indicates the end of the file

# If you want to check the current position of the pointer, you can use the  fileobject.tell()
# method, which returns a decimal value for where the pointer is at in the current file.


with open('ACA_2019_python_lectures/data/a.txt', 'r+') as file_object:
    # the initial point is at the beginning of the file
    print(file_object.tell())

    file_object.seek(38, 0)  # moving 38 characters starting from the beginning of the file
    file_object.write('***')
    print(file_object.tell())  # >>> 41 = 38 + 3

    file_object.seek(0, 2)  # moving to the end
    file_object.write('xxxxxxxxxxxxxx')
    print(file_object.tell())

# Please note that we have changed the file mode to 'r+', because in modes 'a' or 'a+', any writing
# is done at the end of the file, even if at the current moment when the write() function is
# triggered the file's pointer is not at the end of the file: the pointer is moved to the end of
# file before any writing.


# JSON (JavaScript Object Notation) files

# JSON is a lightweight data-interchange format. It is easy for humans to read and write. It is
# easy for machines to parse and generate.

# JSON is built on two structures:

# - A collection of name/value pairs. In various languages, this is realized as an object, record,
#   struct, dictionary, hash table, keyed list, or associative array.
# - An ordered list of values. In most languages, this is realized as an array, vector, list, or
#   sequence.

# In Python it is realized with dictionary.


# Python Supports JSON Natively!

# The process of encoding JSON is usually called serialization. This term refers to the
# transformation of data into a series of bytes (hence serial) to be stored or transmitted across a
# network. What happens after a computer processes lots of information? It needs to take a data
# dump. Accordingly, the json library exposes the dump() method for writing data to files. There i
# s also a dumps() method (pronounced as “dump-s”) for writing to a Python string.

# Simple Python objects are translated to JSON according to a fairly intuitive conversion.

# Python	            JSON
# dict	                object
# list, tuple	        array
# str	                string
# int, long, float	    number
# True	                true
# False	                false
# None	                null


import json

# For reading json file we can use json.load(file_object):
with open("ACA_2019_python_lectures/data/b.json", "r") as file_object:
    data = json.load(file_object)
    print(data)

# For writing json file we can use json.dump(data, file_object):
data = {i: (i ** 2, i ** (1 / 2)) for i in range(4)}
data['new line 1'] = [1, 2.5, True]
data['new line 2'] = {'a': 56}

with open("ACA_2019_python_lectures/data/new_json.json", "w") as file_object:
    json.dump(data, file_object, indent=2)

# Or, if you were so inclined as to continue using this serialized JSON data in your program,
# you could write it to a native Python str object.

json_string = json.dumps(data)
print(json_string)
print(type(json_string))

# CSV (Comma Separated Values) files

# CSV format is the most common import and export format for spreadsheets and databases. This is a
# type of plain text file that uses specific structuring to arrange tabular data. Because it’s a
# plain text file, it can contain only actual text data—in other words, printable ASCII or Unicode
# characters.


# Python Supports CSV Natively!


import csv
from collections import defaultdict

from pprint import pprint

# Reading CSV Files With csv
with open('ACA_2019_python_lectures/data/c.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\nColumn names are \n\t{", ".join(row)}')
            line_count += 1
            print(f'\nLines are \n')
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

# Reading CSV Files Into a Dictionary With csv
data = defaultdict(list)
with open('ACA_2019_python_lectures/data/c.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i, row in enumerate(csv_reader):
        print(type(row))
        for column, value in row.items():
            data[column].append(value)

pprint(data, width=500)

# Writing CSV Files With csv
with open('ACA_2019_python_lectures/data/employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file,
                                 delimiter=',',
                                 quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Name', 'Department', 'Month'])
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
