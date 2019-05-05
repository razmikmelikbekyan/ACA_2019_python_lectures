# Python Capstone Project - Library application

This project suggests that you build an application for managing books library. Application will 
be a console-based tool, which allows librarian to manage available books, add new ones, give books
for reading to users, delete books and so on. 


## Project structure

Project should consists of 2 main parts: **database** package and **app.py**. 


### Database

This package should handle storing data of *books* and *users*. It should contain **books.txt** and
**books.py**, **users.json** and **users.py**.


#### Books


##### books.txt

You should store books in the *books.txt* file. Each line of this file should contain one book 
data:

* *code* - string with length 5, only alphanumeric
* *name* - string with maximum 100 length, only alphanumeric
* *author* - string with maximum 45 length, only alphanumeric
* *quantity* - int, represents number of books in library
* *available quantity* - int, represents number of available books in library

The above mentioned all data for one book should be combined in one big string by using **" $$ "**
as a separator - 

` code $$ name $$ author $$ quantity $$ available quantity`

And this string will be a line of *books.txt* file, for example:

`"a1254 $$ The Idiot $$ Fyodor Dostoyevsky $$ 4 $$ 2"`

Each book must have a unique a code, which will be the main key for manipulating books database.


##### **books.py** 

This module should contain the following functions:

* *create_books_data* - creates an empty *books.txt* file

* *add_book* - adds book to the *books.txt*, it should check constraints on book data (described 
               above) and raise errors with respective message if any of constraint does not met,
               it should check also that there is no book in the library with the same code and 
               raise an error if there is a book with the same code
               
* *delete_book* - deletes book from database, should raise an exception if its quantity and 
                  available quantity are not equal (there are users, who have not returned books)
               
* *find_book* - finds book by given search code, if book is not found returns an empty dict, 
                otherwise returns book data in the form of dict -                
    
    
    {
        'code': 'a1254',
        'name': 'The Idiot',
        'author': 'Fyodor Dostoyevsky',
        'quantity': 4,
        'available_quantity': 2
    } 
                    
* *get_all_books* - returns the list of all books data, where each item of the list is a book data 
                    dictionary (see above example)
                    
* *give_book_to_user* - gives book to user from library: decreases book available_quantity by 1

* *get_book_from_user* - gets book from user back to library: increases book available_quantity by 1


#### Users


##### users.json

You should users and books, which their get from library in a **users.json** file. Each entry of
it should be **user_code: [book_code_1, book_code_2, ...]**.

* *user_code* - string with length 6, only alphanumeric
* *book_code* - this is the same code as described in *books* partaka

##### **users.py** 

This module should contain the following functions:

* *create_users_data* - creates an empty *users.json* file

* *get_all_users* - returns the dictionary, with all users data
aka
* *add_user* - adds user in *users.json* with empty books data: **user_code: []**

* *delete_user* - deletes user from *users.json*, should raise an exception, if user has not aka
                  returned books

* *get_user_books* - returns the list of user's books

* *get_book_from_library* - modifies user's books data by adding a book_code, should raise an 
                            exception, if user is not in database 

* *return_book_to_library* - modifies user's books data by deleting a book_code, should raise an 
                             exception, if user is not in database


### app.py

This is the application runner file, which should be called from console. Please note that it 
will be called directly from project directory: `python app.py [commands]`. You should use python
built in module `argparse` for handling passed commands. It should get the following arguments:

* --o - the operation, which the application user wants to perform: **'get_all_books', 'add_book',
        'find_book', 'delete_book', 'get_all_users', 'add_user', 'get_user_books', 'delete_user',
        'get_book_from_library', 'return_book_to_library'**, this should be required argument and 
        its possible inputs should be restricted by using `choices`
        
* --book - book code

* --name - book name

* --author - book author

* --quantity - book quantity

* --user - user code


### Technical notes

Please note that functions **give_book_to_user** and **get_book_from_user** will not be directly
called from console, instead they should be called with functions **get_book_from_library** and
**return_book_to_library** functions respectively. In other words, when user gets a book from
library you should call the following command from console:
 
```python app.py --o get_book_from_library --user "user_code" --book "book_code"``` 

This command should call 2 functions: **give_book_to_user** and **get_book_from_library**, the 
first one will check the book availability in library, will decrease available quantity by 1 in 
*books.txt* and the second one will add book to user's books data in *users.json* .


Please note also that if you will have troubles when reading an empty json, you should use `try 
except`:

```
with open(USERS, 'r') as infile:
    try:
        return json.load(infile)
    except ValueError:
        return {}
```