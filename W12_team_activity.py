
largest_book = {}
largest_book['chapters'] = 0

largest_mormon_book = {}
largest_mormon_book['chapters'] = 0

largest_interest_scripture = {}
largest_interest_scripture['chapters'] = 0

scripture_str = 'scripture'
chapters_str = 'chapters'
book_str = 'book'

option = input("Which volume of scriptures you would like to learn about?\n"
    "1. Old Testament\n"
    "2. New Testament\n"
    "3. Book of Mormon\n"
    "4. Doctrine and Covenants\n"
    "5. Pearl of Great Price\n"
    "------------\n"
    "Insert the number of the option you choose: ")

if option == '1':
    scripture_query = 'Old Testament'
elif option == '2':
    scripture_query = 'New Testament'
elif option == '3':
    scripture_query = 'Book of Mormon'
elif option == '4':
    scripture_query = 'Doctrine and Covenants'
elif option == '5':
    scripture_query = 'Pearl of Great Price'

with open('./books_and_chapters.txt') as data:
    for book_details in data:
        book, chapters_r, scripture_r = book_details.split(':')
        chapters = int(chapters_r)
        scripture = scripture_r.strip()

        if largest_book['chapters'] < chapters:
            largest_book['book'] = book
            largest_book['chapters'] = chapters
            largest_book['scripture'] = scripture

        if scripture == 'Book of Mormon':
            print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')

            if largest_mormon_book['chapters'] < chapters:
                largest_mormon_book['book'] = book
                largest_mormon_book['chapters'] = chapters
                largest_mormon_book['scripture'] = scripture

        if scripture_query == scripture:

            if largest_interest_scripture['chapters'] < chapters:
                largest_interest_scripture['book'] = book
                largest_interest_scripture['chapters'] = chapters
                largest_interest_scripture['scripture'] = scripture

    print('\n-- Larguest Chapters Book:\n'
        f'Scripture: {largest_book[scripture_str]}, Book: {largest_book[book_str]}, Chapters: {largest_book[chapters_str]}\n')

    print('-- Larguest Chapters Book in the Book of Mormon:\n'
        f'Scripture: {largest_mormon_book[scripture_str]}, Book: {largest_mormon_book[book_str]}, Chapters: {largest_mormon_book[chapters_str]}\n')

    print('-- Larguest Chapters Book in the Book of Mormon:\n'
        f'Scripture: {largest_interest_scripture[scripture_str]}, Book: {largest_interest_scripture[book_str]}, Chapters: {largest_interest_scripture[chapters_str]}\n')
        