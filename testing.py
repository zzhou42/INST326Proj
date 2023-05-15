import unittest
import tkinter as tk
from application import Contact, ContactList, ContactListApp
 

class TestContactMethods(unittest.TestCase):
    "Testing methods in Contact Class"
    
    def test_get_first_name(self):
        "Asserting method returns correct first name"
        
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")   
        self.assertEqual(contact.get_first_name(), "John")

    def test_get_last_name(self):
        
        "Asserting method returns correct last name"
        
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        self.assertEqual(contact.get_last_name(), "Doe")

    def test_get_phone(self):
        
        "Asserting method returns corect phone number"
        
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        self.assertEqual(contact.get_phone(), "1234567890")

    def test_get_email(self):
        
        "Asserting method returns correct email"
        
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        self.assertEqual(contact.get_email(), "johndoe@example.com")

class TestContactListMethods(unittest.TestCase):
    
    "Testing methods in ContactList Class :Asserting method adds a contact to contact list"
    
    def test_add_contact(self):
        contact_list = ContactList()
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        contact_list.add_contact(contact)
        self.assertEqual(contact_list.contacts["John"], contact)

    def test_remove_contact(self):
        
        "Asserting method removes contact from contact list"
        
        contact_list = ContactList()
        contact = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        contact_list.add_contact(contact)
        contact_list.remove_contact("John")
        self.assertEqual(len(contact_list.contacts), 0)

    def test_get_all_contacts(self):
        
        "Asserting method returns all contacts"
        
        contact_list = ContactList()
        contact1 = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        contact2 = Contact("Jane", "Smith", "9876543210", "janesmith@example.com")
        contact_list.add_contact(contact1)
        contact_list.add_contact(contact2)
        contacts = contact_list.get_all_contacts()
        self.assertEqual(len(contacts), 2)
        self.assertIn(contact1, contacts)
        self.assertIn(contact2, contacts)

class TestContactListAppMethods(unittest.TestCase):
    
    "Testing Methods In  ContactListApp Class, (testing if previous methods work with app object created) "
    
    def test_add_contact(self):
        "Asserting Add contact adds a contact"
        
        contact =  Contact("John", "Doe", "1234567890", "johndoe@example.com")
        root = tk.Tk()
        app = ContactListApp(root)
        app.contact_list = ContactList()
        app.contact_list.add_contact(contact)
        self.assertEqual(len(app.contact_list.contacts), 1)

    def test_remove_contact(self):
        "Asserting removing a contact removes contact"
        
        root = tk.Tk()
        app = ContactListApp(root)
        app.contact_list = ContactList()
        contact1 = Contact("John", "Doe", "1234567890", "johndoe@example.com")
        app.contact_list.add_contact(contact1)
        app.contact_list.remove_contact("John")
        self.assertEqual(len(app.contact_list.contacts), 0)



if __name__ == '__main__':
    unittest.main()
