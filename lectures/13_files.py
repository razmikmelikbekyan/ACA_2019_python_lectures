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


# We will introduce pathlib module and parallel will discuss also os.path module.
from pathlib import Path
import os

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




# Creating Multiple Directories
directory_path = '/home/ubuntu/Desktop/ACA/ACA_2019_python_lectures/new_dir/good/directory'

# p = Path(directory_path)
# p.mkdir(parents=True, exist_ok=True)

# Passing parents=True to Path.mkdir() makes it create the directory 05 and any parent directories
# necessary to make the path valid.

os.makedirs(directory_path, exist_ok=True)



# https://dbader.org/blog/python-file-io
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://realpython.com/working-with-files-in-python/
# https://realpython.com/python-pathlib/
