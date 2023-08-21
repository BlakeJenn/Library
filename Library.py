# Author: Blake Jennings
# GitHub username: BlakeJenn
# Email: blakej94@gmail.com
# Description: Creates a Library, LibraryItem(subclass Book, Album, Movie), and Patron Class
# The Library Class has a dictionary of Patron Objects, a Dictionary of LibraryItem Objects, keeps track of the
# current day, and has methods to let Patrons checkout, turn in, and request LibraryItem Objects and pay their
# overdue fine

class LibraryItem:
    """Represents an Item from a Library Class"""

    def __init__(self, library_item_id, title):
        """Initiates a LibraryItem Object with an ID and title"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_location(self):
        """Returns the location of a LibraryItem Object"""
        return self._location

    def set_location(self, location):
        """Assigns the location of a LibraryItem Object"""
        self._location = location

    def get_id(self):
        """Returns the ID number of a LibraryItem Object"""
        return self._library_item_id

    def set_checked_out_by(self, patron):
        """Assigns which Patron Object checked out a LibraryItem Object"""
        self._checked_out_by = patron

    def get_checkout_date(self):
        """Returns the checkout date of a LibraryItem Object"""
        return self._date_checked_out

    def set_checkout_date(self, date):
        """Assigns the checkout date of a LibraryItem Object"""
        self._date_checked_out = date

    def get_requested_by(self):
        """Returns which Patron Object requested a LibraryItem Object"""
        return self._requested_by

    def set_requested_by(self, patron):
        """Assigns which Patron Object requested a LibraryItem Object"""
        self._requested_by = patron


class Book(LibraryItem):
    """Represents a Book from a Library Class (subclass of LibraryItem)"""

    def __init__(self, library_item_id, title, author):
        """Initiates a Book Object with an ID, title and author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Returns the author of a Book Object"""
        return self._author

    def get_checkout_length(self):
        """Returns the maximum amount of days a Book Object can be checked out before fines incur"""
        return 21


class Album(LibraryItem):
    """Represents an Album from a Library Class (subclass of LibraryItem)"""

    def __init__(self, library_item_id, title, artist):
        """Initiates an Album Object with an ID, title, and artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Returns the artist of an Album Object"""
        return self._artist

    def get_checkout_length(self):
        """Returns the maximum amount of days an Album Object can be checked out before fines incur"""
        return 14


class Movie(LibraryItem):
    """Represents a Movie from a Library Class (subclass of LibraryItem)"""

    def __init__(self, library_item_id, title, director):
        """Initiates a Movie Object with an ID, title, and director"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Returns the director of a Movie Object"""
        return self._director

    def get_checkout_length(self):
        """Returns the maximum amount of days a Movie Object can be checked out before fines incur"""
        return 7


class Patron:
    """Represents a Patron who checks out LibraryItem Objects from the Library Class"""

    def __init__(self, patron_id, name):
        """Initiates a Patron Object with an ID and name"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_name(self):
        """Returns the name of a Patron Object"""
        return self._name

    def get_checked_out_items(self):
        """Returns a list of checked out LibraryItem Objects a Patron Object currently has"""
        return self._checked_out_items

    def get_id(self):
        """Returns the ID of a Patron Object"""
        return self._patron_id

    def get_fine_amount(self):
        """Returns the fine amount a Patron Object currently has"""
        return self._fine_amount

    def add_library_item(self, lib_item):
        """Adds a LibraryItem Object to a Patron Object's list of checked out items"""
        self._checked_out_items.append(lib_item)

    def remove_library_item(self, lib_item):
        """Removes a LibraryItem Object to a Patron Object's list of checked out items"""
        self._checked_out_items.remove(lib_item)

    def amend_fine(self, amount):
        """Adds a numeric amount to a Patron Object's fine amount"""
        self._fine_amount += amount


class Library:
    """Represents a Library with LibraryItem Objects and Patron Objects"""

    def __init__(self):
        """Initiates a Library Object with an empty dictionary of LibraryItems and Patrons"""
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def get_current_date(self):
        """Returns the current date"""
        return self._current_date

    def add_library_item(self, lib_item):
        """Adds a LibraryItem Object to the Holdings Dictionary"""
        self._holdings[lib_item.get_id()] = lib_item

    def add_patron(self, patron):
        """Adds a Patron Object to the Members Dictionary"""
        self._members[patron.get_id()] = patron

    def lookup_library_item_from_id(self, lib_item_id):
        """Returns a LibraryItem Object from its ID. If it is not in the Holdings Dictionary, returns None"""
        for item in self._holdings:
            if item == lib_item_id:
                return self._holdings[lib_item_id]
        return None

    def lookup_patron_from_id(self, patron_id):
        """Returns a Patron Object from its ID. If it is not in the Members Dictionary, returns None"""
        for item in self._members:
            if item == patron_id:
                return self._members[patron_id]
        return None

    def check_out_library_item(self, patron_id, lib_item_id):
        """Allows a Patron Object to check out a LibraryItem Object if it is in the Holdings Dictionary and available"""
        if self.lookup_patron_from_id(patron_id) is None:
            return "patron not found"
        elif self.lookup_library_item_from_id(lib_item_id) is None:
            return "item not found"
        elif self._holdings[lib_item_id].get_location() == "CHECKED_OUT":
            return "item already checked out"
        elif self._holdings[lib_item_id].get_location() == "ON_HOLD_SHELF" and self._holdings[lib_item_id].get_requested_by() != self._members[patron_id]:
            return "item on hold by other patron"
        else:
            self._holdings[lib_item_id].set_checked_out_by(self._members[patron_id])
            self._holdings[lib_item_id].set_checkout_date(self._current_date)
            self._holdings[lib_item_id].set_location("CHECKED_OUT")
            self._holdings[lib_item_id].set_requested_by(None)
            self._members[patron_id].add_library_item(self._holdings[lib_item_id])
            return "check out successful"

    def return_library_item(self, lib_item_id):
        """Allows a Patron Object to return a LibraryItem Object"""
        if self.lookup_library_item_from_id(lib_item_id) is None:
            return "item not found"
        elif self._holdings[lib_item_id].get_location() == "ON_SHELF":
            return "item already in library"
        else:
            for member in self._members:
                if self._holdings[lib_item_id] in self._members[member].get_checked_out_items():
                    self._members[member].remove_library_item(self._holdings[lib_item_id])
            if self._holdings[lib_item_id].get_requested_by() is None:
                self._holdings[lib_item_id].set_location("ON_SHELF")
            else:
                self._holdings[lib_item_id].set_location("ON_HOLD_SHELF")
            self._holdings[lib_item_id].set_checked_out_by(None)
            return "return successful"

    def request_library_item(self, patron_id, lib_item_id):
        """Allows a Patron Object to request a LibraryItem Object"""
        if self.lookup_patron_from_id(patron_id) is None:
            return "patron not found"
        elif self.lookup_library_item_from_id(lib_item_id) is None:
            return "item not found"
        elif self._holdings[lib_item_id].get_requested_by() is not None:
            return "item already on hold"
        else:
            self._holdings[lib_item_id].set_requested_by(self._members[patron_id])
            if self._holdings[lib_item_id].get_location() == "ON_SHELF":
                self._holdings[lib_item_id].set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """Allows a Patron Object to pay their fine"""
        if self.lookup_patron_from_id(patron_id) is None:
            return "patron not found"
        self._members[patron_id].amend_fine(-amount_paid)
        return "payment successful"

    def increment_current_date(self):
        """Increases the current day by 1 and incurs fines to Patron Objects if needed"""
        self._current_date += 1
        for member in self._members:
            for item in self._members[member].get_checked_out_items():
                if self._current_date - item.get_checkout_date() > item.get_checkout_length():
                    self._members[member].amend_fine(0.10)

#---------------------- Testing -----------------------------

 b1 = Book("345", "Phantom Tollbooth", "Juster")
 a1 = Album("456", "...And His Orchestra", "The Fastbacks")
 m1 = Movie("567", "Laputa", "Miyazaki")
 print(b1.get_author())
 print(a1.get_artist())
 print(m1.get_director())
      
 p1 = Patron("abc", "Felicity")
 p2 = Patron("bcd", "Waldo")
      
 lib = Library()
 lib.add_library_item(b1)
 lib.add_library_item(a1)
 lib.add_patron(p1)
 lib.add_patron(p2)
      
 lib.check_out_library_item("bcd", "456")
 for _ in range(7):
     lib.increment_current_date()  # 7 days pass
 lib.check_out_library_item("abc", "567")
 loc = a1.get_location()
 lib.request_library_item("abc", "456")
 for _ in range(57):
     lib.increment_current_date()   # 57 days pass
 p2_fine = p2.get_fine_amount()
 lib.pay_fine("bcd", p2_fine)
 lib.return_library_item("456")
