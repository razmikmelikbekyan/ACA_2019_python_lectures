# Introduction to Python simple Project structure


#### Modules

If you quit from the Python interpreter and enter it again, the definitions you have made 
(functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you
are better off using a text editor to prepare the input for the interpreter and running it with 
that file as input instead. This is known as creating a ***script***. As your program gets longer,
you may want to split it into several files for easier maintenance. You may also want to use a 
handy function that you’ve written in several programs without copying its definition into each 
program.

To support this, Python has a way to put definitions in a file and use them in a script or in an 
interactive instance of the interpreter. Such a file is called a ***module*** - the highest-level 
program organization unit, which packages program code and data for reuse (Python definitions and 
statements), and provides self-contained namespaces that minimize variable name clashes across your
programs. In concrete terms, modules typically correspond to Python program files. Each file is a 
module, and modules can import other modules to use the names they define. Modules might also 
correspond to extensions coded in external languages such as C, Java, or C#, and even to 
directories in package imports.


##### Why Use Modules?

Modules have at least three roles:

* *Code reuse*

    Modules let you save code in files permanently and use it where you want.
    
*  *System namespace partitioning*

    Modules are also the highest-level program organization unit in Python. Although they are 
    fundamentally just packages of names, these packages are also self-contained: you can never see
    a name in another file, unless you explicitly import that file.
    
   
* *Implementing shared services or data*

    From an operational perspective, modules are also useful for implementing components that are 
    shared across a system and hence require only a *single copy*. For instance, if you need to 
    provide a global object that’s used by more than one function or file, you can code it in a 
    module that can then be imported by many clients.    
    
    
#### Python Program Architecture


This section introduces the general architecture of Python programs—the way you divide a program 
into a collection of source files (a.k.a. modules) and link the parts into a whole.

At a base level, a Python program consists of text files (with *.py* suffix) containing Python 
statements, with one main *top-level file (a.k.a. script or runner)* , and zero or more 
supplemental files known as *modules*.

Here’s how this works. The top-level file contains the main flow of control of your program—this
is the file you run to launch your application. The module files are libraries of tools used to 
collect components used by the top-level file, and possibly elsewhere. Top-level files use tools 
defined in module files, and modules may use also tools defined in other modules.

Although they are files of code too, module files generally don’t do anything when run directly; 
rather, they define tools intended for use in other files. A file *imports* a module to gain access
to the tools it defines, which are known as its *attributes*—variable names attached to objects 
such as functions. Ultimately, we import modules and access their attributes to use their tools.

In this project sample our program consists of 3 files (*a.py*, *b.py* and *c.py*) and one package
called *helpers*, which itself consists of 3 files (`__init__.py`, *math_tools.py*, *checkers.py*).


The file *a.py* is chosen to be the top-level file; it will be a simple text file of statements,
which is executed from top to bottom when launched. The files *b.py* and *c.py* are modules; they 
are simple text files of statements as well, but they are not usually launched directly. Instead,
as explained previously, modules are normally imported by other files that wish to use the tools 
the modules define. For now let's skip discussion about *helpers* package.

The aim of this sample project is to calculate statistics from input dictionary: sum of dictionary 
values and sum of dictionary squared values. In *b.py* we have 2 functions **parse_string_dict** 
and **calculate_dict_stat**, which should be used in *a.py*. 

To satisfy such goals, *import* (also *from*) statements execute and load other files on request. 
More formally, in Python, cross-file module linking is not resolved until such *import* statements
are executed at runtime; their net effect is to assign module names—simple variables like b —to 
loaded module objects. In fact, the module name used in an import statement serves two purposes: it
identifies the external file to be loaded, but it also becomes a variable assigned to the loaded 
module.

This is how we did it:

```
from b import parse_string_dict, calculate_dict_stat
```

Similarly, objects *defined* by a module are also created at runtime, as the *import* is
executing: import literally runs statements in the target file one at a time to create its
contents. Along the way, every name assigned at the top-level of the file becomes an
attribute of the module, accessible to importers.

The notion of importing is completely general throughout Python. Any file can import tools from any
other file. For instance, the file a.py may import b.py to call its function, but b.py might also 
import c.py (it is actually does it) to leverage different tools defined there.

Please remember that modules are loaded and run on the first **import** or **from** , and only the
first. This is on purpose—because importing is an expensive operation, by default Python does it
just once per file, per process. Later import operations simply fetch the already loaded module 
object. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just 
one module you want to test interactively, use: 

```
import importlib
importlib.reload(modulename)
```


#### Executing modules as scripts


Please not that *a.py*, which is chosen to be a top-level file or script, is module itself. 
When we run the it with:
 
 ```
 python a.py
 ```
 
the code in the module will be executed, just as if you imported it, but with the `__name__` set to
`__main__`. That means that by adding this code at the end of your module:

```
if __name__ == "__main__":
    ...
```

you can make the file usable as a script as well as an importable module, because the code that 
parses the command line only runs if the module is executed as the “main” file.



#### Standard Library Modules


Some of the modules that your programs will import are provided by Python itself and are not files
you will code. For example *ast*, *typing*, *math* and etc. Python automatically comes with a large
collection of utility modules known as the *standard library*. This collection, over 200 modules 
large at last count, contains platform-independent support for common programming tasks: operating 
system interfaces, object persistence, text pattern matching, network and Internet scripting, GUI
construction, and much more (for more details: https://www.python.org/). None of these tools are 
part of the Python language itself, but you can use them by importing the appropriate modules on 
any standard Python installation. Because they are standard library modules, you can also be
reasonably sure that they will be available and will work portably on most platforms on which you 
will run Python.


#### Module Packages

Now lets talk about *package helpers*. A directory of Python code is said to be a *package*, so 
such imports are known as *package imports*. In effect, a package import turns a directory on your
computer into another Python namespace, with attributes corresponding to the subdirectories and 
module files that the directory contains.

At a base level, package imports are straightforward—in the place where you have been
naming a simple file in your import statements, you can instead list a path of names
separated by periods:
```
import helpers.utils.math_tools
```

The “dotted” path in these statements is assumed to correspond to a path through the directory
hierarchy on your computer, leading to the file *mod.py*. That is, the preceding statements
indicate that on your machine there is a directory *dir1*, which has a subdirectory *dir2*, which 
contains a module file *mod.py* (or similar).

We can use also `__init__.py` file for *package imports*: if the package main directory contains
`__init__.py`, we can use the following syntax for *package* imports: 

```
import helpers
```

In this case we actually will import the `__init__.py ` located directly in *helpers* directory.
In order to be able to import modules defined in *helpers*, its `__init__.py` should imports 
*helpers* modules itself.


As an advanced feature, you can use `__all__` lists in `__init__.py` files to define what is 
exported when a directory is imported with the from * statement form. In an `__init__.py` file, the
`__all__` list is taken to be the list of submodule names or submodule attributes that should be 
automatically imported when from * is used on the package (directory) name.