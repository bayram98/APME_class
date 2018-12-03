"""
Your objective is to implement a simple Phone Book.
Phone numbers are stored in a dictionary, e.g. { "Adam" : "010-0000-1111", "Alice" : "010-0011-2233"}
See the code in the main for an example of how the phone book can be used
"""



def add_contact(phone_book, name, number):
    """
    This function allows to store a new contact in the phone book
    :param phone_book: the phone book (dictionary)
    :param name: the name of the contact (a string)
    :param number: the cell number of the contact (a string)
"""
    phone_book[name] = number;


def search_contact(phone_book, name):
    """
    This functions allows to search for a contact. It should print a meaningful message, e.g.:
    "Contact "Alice" found: 010-1111-2222" OR
    "Contact Alice not found!"
    This function should also return the boolean value True if the contact is found, False otherwise
    :param phone_book: the phone book (dictionary)
    :param name: the name of the contact to search
    """
    if name in phone_book.keys():                                           # test if key exists in dictionary
        print("Contact {0} found: {1}".format(name, phone_book[name]))
        return True
    else:
        print("Contact {0} not found".format(name))
        return False

def delete(phone_book, name):
    """
    This function deletes a contact from the phone book (note: you should manage also the case in which the
    contact to delete is not in the phone book!)
    :param phone_book: the phone book (dictionary)
    :param name: he name of the contact to search
    """
    if name in phone_book.keys():
        del phone_book[name]

def count_contacts(phone_book):
    """
    This function counts the number of contacts in the phone book and prints a message, e.g.:
    "The number of contacts is: 25"
    :param phone_book: the phone book (dictionary)
    """
    print("The number of contacts is : {0}".format(len(phone_book)))

def print_phone_book(phone_book):
    """
    This function prints on the console the content of the entire phone book
    :param phone_book: the phone book (dictionary)
    """
    print(phone_book)

# ADDITIONAL
def find_number(phone_book, number):
    pass

def add_list_of_contacts_v1(phone_book, names, numbers):
    pass

def add_list_of_contacts_v2(phone_book, new_contacts):
    pass

def print_entries_start_with(phone_book, letters):
    pass


if __name__ == '__main__':
    """ use the code below to test your implementation """

    # phone book initialised:
    phone_book = {"John" : "010-6787-990011", "Jin" : "010-4455-7788", "Bob" : "010-8872-0011"}

    print_phone_book(phone_book)                                # print the phone book content
    add_contact(phone_book, "Alice", "010-7865-8899")           # add one entry
    search_contact(phone_book, "Jiyoung")                         # search for Jyoung's number
    search_contact(phone_book, "Jin")                             # search for Jin's number
    count_contacts(phone_book)                                   # should output 4
    delete(phone_book, "Bob")                                   # delete Bob from the phone book
    delete(phone_book, "Alice")
    add_contact(phone_book, "Marco", "010-9988-6677")
    count_contacts(phone_book)                                   # should output 3
    print_phone_book(phone_book)


