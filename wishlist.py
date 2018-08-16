#Main program

import ui, datastore
from book import Book


def handle_choice(choice):
    """ Call appropriate function to respond to user's choice, or error message if choice is invalid """

    if choice in menu_functions:
        menu_functions[choice]()   # Invoke function from dictionary

    else:
        ui.message('Please enter a valid selection')


# These three functions seem a little redundant, but makes it easier to store
# a function name in a dictionary

def show_unread():
    show_books(False)


def show_read():
    show_books(True)


def show_books(read=None):
    """ Fetch and show books from datastore. Default is to show all books. Use read argument to specify only read books or only unread books. """
    books = datastore.get_books(read=read)
    ui.show_list(books)


def mark_book_read():
    """ Get choice from user, edit datastore, display success/error """

    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    """ Get info from user, add new book """

    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def quit():
    """ Perform shutdown tasks """

    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


# Menu options, and function name to run in response to that selection.
menu_functions = {
    '1': show_unread,
    '2': show_read,
    '3': mark_book_read,
    '4': new_book,
    'q': quit
}


if __name__ == '__main__':
    main()
