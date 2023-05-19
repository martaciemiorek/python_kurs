def book_rating():
    books = {
        "1": {"title": "Harry Potter and the Philosopher's Stone", "rating": 4.5},
        "2": {"title": "To Kill a Mockingbird", "rating": 4.3},
        "3": {"title": "Pride and Prejudice", "rating": 4.2},
        "4": {"title": "The Great Gatsby", "rating": 4.1},
        "5": {"title": "1984", "rating": 4.0},
    }
    book_num = input("Enter book number (1-5): ")
    if book_num in books:
        print("Book title:", books[book_num]["title"])
        print("Book rating:", books[book_num]["rating"])
    else:
        print("Invalid book number")