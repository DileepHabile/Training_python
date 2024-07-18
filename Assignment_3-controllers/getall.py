import json
def get_all_books():
    try:
        with open("books.json", 'r') as books_list:
                data = json.load(books_list)
                return data  
    except Exception as e:
        print(f"Unexpected error: {e}")
        return [] 
