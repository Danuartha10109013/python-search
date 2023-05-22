# Percobaan 6
def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()

    if title1[0] == title2[0] :
        return True

    return False
def sequential_search(books, book_title) :
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']

    return "Buku tidak ditemukan"
books = [
    { 'title': 'Python Programing', 'shelf': 'A1'},
    {'title':'Data Structures and Algorithms', 'shelf': 'B2'},
    {'title': 'Introduction to machine Learning' , 'shelf': 'C3'},
    { 'title': 'Database Manageænt Systems', 'shelf': 'D4'}
]

book_title = input("Masukan judul buku yang ingin dicari: ")
Shelf_location = sequential_search(books, book_title)
print(Shelf_location)
