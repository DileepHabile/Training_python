from getall import get_all_books
from getbook import get_detailsof_book
from edit_details import edit_book
from create_book import create_book
from delete_book import delete_book_details
id_value='c2a4ce78-30f8-4519-9872-93f81769e496'

books1=get_all_books()
print(books1)
print('------------------------------------------------------')



books2=get_detailsof_book(id_value)
print(books2)
print('--------------------------------------------------------')

books3=edit_book(id_value)
print('---------------------------------------------------------')

books4=create_book()
print('-----------------------------------------------------------')

books5=delete_book_details(id_value)
print(books5)
print('-------------------------------------------------------------')

books6=get_all_books()
print(books6)
print('---------------------------------------------------')
print('All the operations are being done ')