"""
Assignment: Final Project
Date: 4_21_23

Colin Clifford - Group Leader, Database, Navigator
Chima Okere - Database, Debugger/Tester
Ken Nguyen - UI/GUI, Debugger/Tester
Zhen Zhou - Navigator, UI/GUI

Create an application where users are able to create/edit an account 
and store contact information through a user interface. This application 
will allow users to have an organized database of their contacts, 
allowing users to not have to frantically look for a specific contact. 
They would have all their contact information with a click of a few buttons.

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Clicking the Login button multiple times causes duplication of the contact 
buttons. Find a way to not let that happen, either create a separate window
for the ContactListApp, or prevent the use of login button when sucessfully
logged in.
- Fix and polish up the ContactListApp, the show_contacts() function needs to be
polished. The printed out contacts list needs to be readable.
- Connect a separate contact list per login user. So if we have 3 users logins
we need 3 separate contact list. We can ditch this if it is too complicated.
Probably talk to TA or Professor about this.
- Organization, this version of code is not optimized and was just me splurging
and testing the limits of tkinter.
- Figure out how to properly use Toplevel() function, or ways to open up multiple
windows and better organize them or visualize them first

- I like Chima's classes he made, Try to modify the GUI aspect of the code with
Chima's classes that he created. Should discuss together.

Code Version: 5.2.23 (Date Last Updated)

"""
"""
Start of Chima's edit---------------------------------------------------------"""
# class Contact:
#     def __init__(self, first_name, last_name, phone_number, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.email = email


# class Login:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.contact_list = ContactList()

        
# class ContactList: #Address Book
#     def __init__(self, contact=None):
#         self.contacts = []
#         if contact is not None: # So No Empty Contacts Allowed
#             self.contacts.append(contact)
            
#     def add_contact(self, contact):
#         self.contacts.append(contact)
        
#     def delete_contact(self, contact):
#         self.contacts.remove(contact)


# class login_list: #Saves Login information
#     def __init__(self, login=None):
#         self.logins = []
#         if login is not None:
#             self.logins.append(login)
            
#     def add_login(self, login):
#         self.logins.append(login)
        
#     def delete_login(self, login):
#         self.logins.remove(login)

"""
End of Chima's edit---------------------------------------------------------"""

"""
Start of Zhen's code--------------------------------------------------------"""
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.first_name] = contact

    def remove_contact(self, first_name):
        if first_name in self.contacts:
            del self.contacts[first_name]
        else:
            messagebox.showerror("Contact not found", "Contact not found")

    def get_all_contacts(self):
        return self.contacts.values()
    
login_list = {"admin":"password"}

class StartWindow:
    def __init__(self, login_root):
        self.login_root = login_root
        self.login_root.geometry("300x400")
        self.login_list = login_list
        
        self.login_frame = tk.Frame(self.login_root)
        self.login_frame.pack()

        self.signup_frame = tk.Frame(self.login_root)
        self.signup_frame.pack()
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(self.signup_frame, text="Signup", command=self.signup)
        self.signup_button.pack()

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_entry = tk.Entry(self.login_frame)
        self.password_entry.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in login_list:
            if password == login_list[username]:
                ContactListApp(root)
                ContactList()
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid username or password")
            
    def signup(self):
        self.signup_window = tk.Toplevel()
        self.signup_window.geometry("300x500")
        self.signup_window.title("Signup")
        
        self.username_signup_label = tk.Label(self.signup_window, text="Username")
        self.username_signup_label.pack()
        
        self.username_signup_entry = tk.Entry(self.signup_window)
        self.username_signup_entry.pack()
        
        self.password_signup_label = tk.Label(self.signup_window, text="Password")
        self.password_signup_label.pack()
        
        self.password_signup_entry = tk.Entry(self.signup_window, show="*")
        self.password_signup_entry.pack()
                
        def signup_save():
            username = self.username_signup_entry.get()
            password = self.password_signup_entry.get()
        
            if username not in login_list:
                login_list[username] = password
            else:
                messagebox.showerror("Error", "Username already exist")
                
            self.signup_window.destroy()
                
        self.signup_done_button = tk.Button(self.signup_window, text="Done", command=signup_save)
        self.signup_done_button.pack()

    def run(self):
        self.login_root.mainloop()

class ContactListApp:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.contact_list = ContactList()

        self.contacts_frame = tk.Frame(self.root)
        self.contacts_frame.pack()

        self.add_contact_button = tk.Button(self.contacts_frame, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack()

        self.remove_contact_button = tk.Button(self.contacts_frame, text="Remove Contact", command=self.remove_contact)
        self.remove_contact_button.pack()

        self.show_contacts_button = tk.Button(self.contacts_frame, text="Show Contacts", command=self.show_contacts)
        self.show_contacts_button.pack()
    


    def add_contact(self):
        add_contact_window = tk.Toplevel(self.root)
        add_contact_window.title("Add Contact")

        first_name_label = tk.Label(add_contact_window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(add_contact_window)
        first_name_entry.pack()

        last_name_label = tk.Label(add_contact_window, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(add_contact_window)
        last_name_entry.pack()

        phone_label = tk.Label(add_contact_window, text="Phone Number:")
        phone_label.pack()
        phone_entry = tk.Entry(add_contact_window)
        phone_entry.pack()

        email_label = tk.Label(add_contact_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(add_contact_window)
        email_entry.pack()

        def save_contact():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone_number = phone_entry.get()
            email = email_entry.get()
            contact = Contact(first_name, last_name, phone_number, email)
            self.contact_list.add_contact(contact)
            messagebox.showinfo("Add Contact", "Contact added successfully")
            add_contact_window.destroy()

        save_button = tk.Button(add_contact_window, text="Save", command=save_contact)
        save_button.pack()

    def remove_contact(self):
        remove_contact_window = tk.Toplevel(self.root)
        remove_contact_window.title("Remove Contact")

        first_name_label = tk.Label(remove_contact_window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(remove_contact_window)
        first_name_entry.pack()

        def remove():
            first_name = first_name_entry.get()
            self.contact_list.remove_contact(first_name)
            remove_contact_window.destroy()

        remove_button = tk.Button(remove_contact_window, text="Remove", command=remove)
        remove_button.pack()
   
  
   
    def show_contacts(self):
        contacts = self.contact_list.get_all_contacts()

        if not contacts:
            messagebox.showinfo("Contact List", "No contacts to show")
            return

        show_contacts_window = tk.Toplevel(self.root)
        show_contacts_window.title("Contact List")

        listbox = tk.Listbox(show_contacts_window, width=70)
        listbox.pack(padx=10, pady=10)

        listbox.insert(tk.END, f"{'First Name':<15}{'Last Name':<15}{'Phone Number':<15}{'Email':<30}")
        listbox.insert(tk.END, "-" * 75)

        for contact in contacts:
            listbox.insert(tk.END, f"{contact.first_name:<15}{contact.last_name:<15}{contact.phone_number:<15}{contact.email:<30}")

        listbox.configure(state="disabled")


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StartWindow(root)
    app.run()


"""
End of Zhen's code--------------------------------------------------------"""
"""
Start of Ken's code---------------------------------------------------------
"""
# class Contact:
#     def __init__(self, first_name, last_name, phone_number, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.email = email

# class ContactBook:
#     def __init__(self):
#         self.contacts = {}
        
#     def display_menu():
#         "Displays the menu options"
#         print "---------- Contact Book ------------"
#         print "Add New Contact"
#         print "Display Contact book"
#         print "Search For Contact"
    
#     def search_contact(name):
#         "Searches for a given name and return 0 if not found"
#         for i in contacts:
#             if(contacts[i][0] == name):
#                 return i
#             return 0
        
#     def add_new_contact():
#         "Adds a new contact to the Contact book"
#         name = raw_input("Name:")
#         address = raw_input("Address:")
#         phone = raw_input("Phone:")
#         email = raw_input("Email:");
#         contacts[len(contacts)+1] = [name,address,phone,email]
#         write_file()
        
# class ContactListApp:
#     def write_file():
#         "Writes the contact details to a file"
#         file = open("contact.txt","w")
#         for i in contacts:
#             file.write("\n".join(contacts[i]))
#             file.write("\n");
#             file.close();
    
#     def read_to_dict():
#         "Reads all the contact details to a dict"
#         file = open("contact.txt","r")
#         text = file.read()
#         textl = text.split("\n")
#         print textl
#         factor = 0
#         contact = []
#         for i in textl:
#             if(factor==4):
#                 contacts[len(contacts)+1] = contact
#                 contact = []
#                 contact.append(i)
#                 factor=1
#                 else:
#                     contact.append(i)
#                     factor += 1
#                     file.close()
                    
#     if __name__ == "__main__":
        
#         app = Main()
#         app.mainloop()
# """
# End of Ken's code--------------------------------------------------------"""
# """
