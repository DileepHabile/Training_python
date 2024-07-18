import json

def get_detailsof_book(id_value):
    try:
        with open("books.json", 'r') as books_list:
            data = json.load(books_list)
            for book in data:
                if book.get('book_id') == id_value:
                    return book
        # If no book with the specified id_value is found
        return None
    except FileNotFoundError:
        print("Error: File 'books.json' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

