# Python Capstone Project - Library application

This project suggests you build an application for managing books library. Application will be a
console-based which will allow librarian to manage available books, add new ones, give books for 
reading to users, delete books and so on. 


## Project structure

Project should consists of 2 main parts: **database** package and **app.py**.   


### Database

This package should handle storing data of *books* and *users*. It should contain **books.txt** and
**books.py**, **users.json** and **users.py**.

#### Books

You should store books in a *books.txt* file. Each line of this file should contain one book data:

* *code* - string with length 5, only alphanumeric
* *name* - string with maximum 100 length, only alphanumeric
* *author* - string with maximum 45 length, only alphanumeric
* *quantity* - int, represents number of books in library
* *available quantity* - int, represents number of available books in library

One book all data should be combined in one big string with **" $$ "** as separator between 
different data - 

` code $$ name $$ author $$ quantity $$ available quantity`

For example:

`"a1254 $$ The Idiot $$ Fyodor Dostoyevsky $$ 4 $$ 2"`

Each book must have a unique a code, which will be the main key for manipulating books database.

**books.py** should contain the following functions:

* *create_books_data* - creates an empty *books.txt* file

* *add_book* - adds book to the *books.txt*, it should check constraints on book data (described 
               above) raise errors with respective message if any of constraint does not met,
               it should check also that there is no book in the library with the same code and 
               raise an error if there is a book with the same code
               
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
                    
* *delete_book* - deletes book from database

* *give_book_to_user* - gives book to user from library: aka decreases book available_quantity by 1
* *get_book_from_user* - gets book from user back to library: aka increases book 
                         available_quantity by 1


#### Users

You should users and books, which their get from library in a **users.json** file. Each entry of
it should be **user_code: [book_code_1, book_code_2, ...]**.

* *user_code* - string with length 6, only alphanumeric
* *book_code* - this is the same code as described in *books* part

**users.py** should contain the following functions:

* *create_books_data* - creates an empty *books.txt* file

* *add_book* - adds book to the *books.txt*, it should check constraints on book data (described 
               above) raise errors with respective message if any of constraint does not met,
               it should check also that there is no book in the library with the same code and 
               raise an error if there is a book with the same code
               
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
                    
* *delete_book* - deletes book from database

* *give_book_to_user* - gives book to user: aka decreases book available_quantity by 1
* *give_book_to_user* - gives book to user: aka decreases book available_quantity by 1