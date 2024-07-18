import json

new_book = {
    "book_id": "e27a30c2-6cbb-46a4-9d8f-b0a443753372",
    "title": "The bravest man of the sea",
    "author": "Usopp",  
    "publications": "tofoei_fear", 
    "website": "animesuge_fear"
}

def create_book():
    try:
        with open('books.json', 'r') as books_file:
            data = json.load(books_file)  
    except FileNotFoundError:
        data = []


    data.append(new_book)

    try:
    
        with open("books.json", 'w') as books_file:
            json.dump(data, books_file, indent=4)  
            print(f"Book '{new_book['title']}' added successfully.")
    except Exception as e:
        print(f"Error in creating a new_book  in 'books.json': {e}")

