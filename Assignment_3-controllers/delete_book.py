import json

def delete_book_details(id_value):
    try:
        with open("books.json", 'r') as books_file:
            data = json.load(books_file)
    except FileNotFoundError:
        print("Error: File 'books.json' not found.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    
    updated_data = []
    for book in data:
        if book['book_id'] != id_value:
            updated_data.append(book)


    try:
        with open('books.json', 'w') as books_file:
            json.dump(updated_data, books_file, indent=4)
            print(f"Book with id {id_value} deleted successfully.")
    except Exception as e:
        print(f"Error writing to 'books.json': {e}")


