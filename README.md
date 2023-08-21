# Library
A Library database that holds books, patrons, a log of patron's checkouts, and library fines.

This is a Library simulator involving multiple classes. It entails LibraryItem, Patron and Library classes, and the three classes that inherit from LibraryItem (Book, Album and Movie). 

Here are descriptions of the three classes:

LibraryItem:

A LibraryItem object represents a library item that a patron can check out from a library. It has six data members:

library_item_id - a unique identifier for a LibraryItem - you can assume uniqueness, you don't have to enforce it
title - cannot be assumed to be unique
location - a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
checked_out_by - refers to the Patron who has it checked out (if any)
requested_by - refers to the Patron who has requested it (if any); a LibraryItem can only be requested by one Patron at a time
date_checked_out - when a LibraryItem is checked out, this will be set to the current_date of the Library

The LibraryItem methods are:

init method - takes a library item ID and title as parameters; checked_out_by and requested_by should be initialized to None; a new LibraryItem's location should be on the shelf
get_location returns the Library Item's location
other get and set methods as needed

Book/Album/Movie:

These three classes all inherit from LibraryItem
All three have an additional data member. For Book, it's a string called author. For Album, it's a string called artist. For Movie, it's a string called director
Each of the new data members have a get method to return its value
All three have a method called get_check_out_length that returns the number of days that type of library item may be checked out for. For a Book it's 21 days, for an Album it's 14 days, and for a Movie it's 7 days

Patron:

A Patron object represents a patron of a library. It has four data members:

patron_id - a unique identifier for a Patron - you can assume uniqueness, you don't have to enforce it
name - cannot be assumed to be unique
checked_out_items - a collection of LibraryItems that a Patron currently has checked out
fine_amount - how much the Patron owes the Library in late fines (measured in dollars); this is allowed to go negative
The Patron methods are:

init method - takes a patron ID and name as parameters
get_fine_amount - returns the fine_amount
other get and set methods as needed
add_library_item - adds the specified LibraryItem to checked_out_items
remove_library_item - removes the specified LibraryItem from checked_out_items
amend_fine - a positive argument increases the fine_amount, a negative one decreases it; this is allowed to go negative

Library:

A Library object represents a library that contains variaous library items, and is used by various patrons. It has three data members:

holdings - a collection of the LibraryItems that belong to the Library
members - a collection of the Patrons who are members of the Library
current_date - stores the current date represented as an integer number of "days" since the Library object was created

The Library methods are:

an init method that initializes the holdings and members as empty collections and initializes the current_date to zero
add_library_item - takes a LibraryItem object as a parameter and adds it to the holdings
add_patron - takes a Patron object as a parameter and adds it to the members
lookup_library_item_from_id - returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in the holdings
lookup_patron_from_id - returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member
check_out_library_item
takes as parameters a patron ID and a library item ID, in that order
if the specified Patron is not in the Library's members, return "patron not found"
if the specified LibraryItem is not in the Library's holdings, return "item not found"
if the specified LibraryItem is already checked out, return "item already checked out"
if the specified LibraryItem is on hold by another Patron, return "item on hold by other patron"
otherwise update the LibraryItem's checked_out_by, date_checked_out and location
if the LibraryItem was on hold for this Patron, update requested_by
update the Patron's checked_out_items
return "check out successful"
return_library_item
takes as its parameter a library item ID
if the specified LibraryItem is not in the Library's holdings, return "item not found"
if the LibraryItem is not checked out, return "item already in library"
update the Patron's checked_out_items
update the LibraryItem's location depending on whether another Patron has requested it (if so, it should go on the hold shelf)
update the LibraryItem's checked_out_by
return "return successful"
request_library_item
takes as parameters a patron ID and a library item ID, in that order
if the specified Patron is not in the Library's members, return "patron not found"
if the specified LibraryItem is not in the Library's holdings, return "item not found"
if the specified LibraryItem is already requested, return "item already on hold"
update the LibraryItem's requested_by
if the LibraryItem is on the shelf, update its location to on hold
return "request successful"
pay_fine
takes as parameters a Patron ID and the amount (in dollars) being paid (in that order)
if the specified Patron is not in the Library's members, return "patron not found"
use amend_fine to update the Patron's fine; return "payment successful"
increment_current_date
takes no parameters
increment current date
increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (by calling amend_fine)
