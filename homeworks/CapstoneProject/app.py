import argparse

from database.books import create_books_data, add_book

parser = argparse.ArgumentParser()

parser.add_argument('--o', choices=['add_book'])
parser.add_argument('--code')
parser.add_argument('--name')
parser.add_argument('--author')
parser.add_argument('--quantity', type=int)





if __name__ == '__main__':
    args = parser.parse_args()
    create_books_data()

    if args.o == 'add_book':
        add_book(args.code, args.name, args.author, args.quantity)

