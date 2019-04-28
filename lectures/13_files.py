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
# editor without any special handling. Still, every text file must adhere to a set of rules:
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
# file_object = open(file path, mode)

# The mode in the open function tells Python what you want to do with the file.
# There are multiple modes that you can specify when dealing with text files.
#
# 'w' –  Write Mode: This mode is used when the file needs to be altered and information changed or
#        added. Keep in mind that this erases the existing file to create a new one.
#        File pointer is placed at the beginning of the file.
# 'r' –  Read Mode: This mode is used when the information in the file is only meant to be read and
#        not changed inany way. File pointer is placed at the beginning of the file.
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

file_object = open('ACA_2019_python_lectures/data/a.txt', 'r+')
print(file_object)
print(type(file_object))

import sys

a= sys.getsizeof(file_object)
print(a)



# https://dbader.org/blog/python-file-io
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://realpython.com/working-with-files-in-python/
# https://realpython.com/python-pathlib/
# https://www.programiz.com/python-programming/file-operation
# https://docs.python.org/3.6/tutorial/inputoutput.html
# https://docs.python.org/3.6/library/io.html#module-io
