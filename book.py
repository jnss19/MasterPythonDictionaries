# Dictionaries of books
books = {
'book1': {
'title': 'Noli Me Tangere',
"author": "Jose Rizal"
},
'book2': {
'title': 'Smaller and Smaller Circles",
"author": "F. H. Batacan"
},
'book3': {
'title': 'Po-on',
"author": "F. Sionil José"
},
'book4': {
'title': 'ABNKKBSNPLAKO?1',
"author": "Bob Ong"
},
'books': {
'title': 'Banaag at Sikat',
"author": "Lope K. Santos"
}
}

# Function to display book details
def display_books(book_dict):
    print("Books:")
    for key, details in book_dict.items():
        print(f"{key}: Title: '{details['title']}', Author: {details['author']}")

# Display the books
display_books(books)
