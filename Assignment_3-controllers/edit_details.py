import json

def edit_book(id_value):
    edit_title = input('Enter the Title of the book: ')
    edit_author = input('Enter the Author of the book: ')
    edit_publications = input('Enter the Publications of the book: ')
    edit_website = input('Enter the Website of the book: ')

    try:
        with open("books.json", 'r+') as books_file:
            data = json.load(books_file)
            for book in data:
                if book['book_id'] == id_value:
                    book['title'] = edit_title
                    book['author'] = edit_author 
                    book['publications'] = edit_publications 
                    book['website'] = edit_website
                    print('The details are being edited.')
                  
                    books_file.seek(0)
                    
                    json.dump(data, books_file, indent=4)
                    return
            print(f'Book with id {id_value} not found.')
    except FileNotFoundError:
        print("Error: File 'books.json' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

