
my_list=[1,6,7,22,3,4,9,10]

#---exercise 1---
def filter_list(numbers:list, integer:int):
    newlist = [x for x in my_list if x > integer]
    return newlist

#print(filter_list(my_list,2))

#---exercise 2---
def count_vowels(text:str):
    count = 0
    for x in text:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            count += 1
    return count

#print(count_vowels('hello'))

#---exercise 3---
def replace_char(text:str, char:str, replace_char:str):
    if char in text:
        return text.replace(char,replace_char)
    else:
        print(f"\"{char}\" is not an occurrence in \"{text}\". The string remains unchanged.")
        return text

#print(replace_char("catch","c","k"))

#---exercise 4---
def hamming(text1:str,text2:str):
    if len(text1) != len(text2):
        print("Strings must be of same length.")
        return 0
    else:
        dist = 0
        for i, x in enumerate(text1):
            if x != text2[i]:
                dist += 1
        return dist

#print(hamming("hat","cat"))

#---exercise 5---
class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return self.name + ", " + self.author

book1 = Book('Dune', 'Frank Herbert')
book2 = Book('The Dark Tower', 'Stephen King')
book3 = Book('Dune Messiah', 'Frank Herbert')
print(book2)

#---exercise 6---
class BookShelf:

    def __init__(self, books):
        self.books = books

    def add_book(self,book):
        self.books.append(book)

    def add_books(self,book):
        self.books.extend(book)

    def books_by_author(self, author):
        authors = []
        for i,x in enumerate(self.books):
            if self.books[i].author == author:
                authors.append(self.books[i].name)
        if authors == []:
            print("There are no books of this author in this bookshelf")
        else:
            print(f"Books by {author}:")
        return authors

    def get_books(self):
        book_names = []
        for i,x in enumerate(self.books):
            book_names.append(self.books[i].name)
        if book_names == []:
            print("Your bookshelf is currently empty:")
        else:
            print("Your books:")
        return book_names

    def clear_shelf(self):
        self.books.clear()
        print("Your bookshelf has been emptied.")

def having_fun_with_books():
    #creating a bookshelf and adding individual books to it
    shelf = BookShelf([])
    shelf.add_book(book1)
    shelf.add_book(book2)
    shelf.add_book(book3)

    #books by author
    print(shelf.books_by_author("Frank Herbert"))

    #show shelf before and after emptying it
    print(shelf.get_books())
    shelf.clear_shelf()
    print(shelf.get_books())

    #create a list of books
    booklist = []
    booklist.append(book1)
    booklist.append(book2)
    booklist.append(book3)

    #show shelf after adding multiple books at once
    shelf.add_books(booklist)
    print(shelf.get_books())

#having_fun_with_books()