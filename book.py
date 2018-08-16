class Book:

    """ Represents one book in a user's list of books """

    NO_ID = -1   # Useful for books with no ID assigned (yet)

    def __init__(self, title, author, read=False, id=NO_ID):
        """ Default new book is unread, and has no ID """

        self.title = title
        self.author = author
        self.read = read
        self.id = id


    def __str__(self):
        """ User-friendly string with all book info """

        read_str = 'yes' if self.read else 'no'  # Use 'yes' and 'no' instead of True and False

        id_str = self.id if self.id is not self.NO_ID else '(no id)'  # Replace the NO_ID value with a user-friendly string

        template = 'id: {} Title: {} Author: {} Read: {}'
        return template.format(id_str, self.title, self.author, read_str)


    def __eq__(self, other):
        """ enables comparing two Book objects using == in code """

        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id
