
import sqlite3

# Connect to the library database
connection = sqlite3.connect("library.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Drop the books table if it already exists
cursor.execute("DROP TABLE IF EXISTS books")

# Create the books table
cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT
)
""")

# Insert all 10 books into the database
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian Fiction"),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy"),
    ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, "Magical Realism"),
    ("The Hitchhikers Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction"),
    ("The Handmaids Tale", "Margaret Atwood", 1980, "Dystopian Fiction"),
    ("War and Peace", "Leo Tolstoy", 1869, "Fiction"),
    ("Ulysses", "James Joyce", 1922, "Fiction")
]

cursor.executemany("""
INSERT INTO books (title, author, publication_year, genre)
VALUES (?, ?, ?, ?)
""", books)

# Print out all books in the table
cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()
print("Printing out all books in the table")
print(all_books)

# Select all books with the Fiction genre
cursor.execute("SELECT * FROM books WHERE genre = 'Fiction'")
fiction = cursor.fetchall()
print("\nSelecting all fiction books")
print(fiction)

# Update The Handmaids Tale publication year to 1985
cursor.execute("""
UPDATE books
SET publication_year = 1985
WHERE title = 'The Handmaids Tale'
""")

# Display The Handmaids Tale after updating
cursor.execute("""
SELECT * FROM books
WHERE title = 'The Handmaids Tale'
""")
updated_book = cursor.fetchall()
print("\nValue after updating publication year of The Handmaids Tale")
print(updated_book)

# Delete the book 1984 from the database
cursor.execute("DELETE FROM books WHERE title = '1984'")

# Print all remaining books after deleting 1984
cursor.execute("SELECT * FROM books")
remaining_books = cursor.fetchall()
print("\nPrinting out all books in the table after deleting 1984")
print(remaining_books)

# Save all database changes
connection.commit()

