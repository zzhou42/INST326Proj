"""
Assignment: Final Project
Date: 4_21_23

Colin Clifford - Group Leader, Database, Navigator
Chima Okere - Database, Debugger/Tester
Ken Nguyen - UI/GUI, Debugger/Tester
Zhen Zhou - Navigator, UI/GUI
start of Main Code"""
import tkinter as tk
from tkinter import messagebox

class Contact:
    """A class which stores attributes relating to an Contact
    
    Attributes:
            first_name (str): the first name of the person you're creating a contact for
            last_name (str): the last name of the person you're creating a contact for
            phone_number (str): the phone number  of the person you're creating a contact for
            email (str): the email of the person you're creating a contact for
    """
    def __init__(self, first_name, last_name, phone_number, email):
        """Initializes an Contact object
    
            Attributes:
                first_name (str): the first name of the person you're creating a contact for
                last_name (str): the last name of the person you're creating a contact for
                phone_number (str): the phone number  of the person you're creating a contact for
                email (str): the email of the person you're creating a contact for
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
    def get_first_name(self):
        """Represent the first name as a string
        
        Returns:
            str: returns a representation of the first name
        """
        return self.first_name
    
    def get_last_name(self):
        """Represent the last name as a string
        
        Returns:
            str: returns a representation of the last name
        """
        return self.last_name
    
    def get_phone(self):
        """Represent the phone number as a string
        
        Returns:
            str: returns a representation of the phone number
        """
        return self.phone_number
    
    def get_email(self):
        """Represent the email as a string
        
        Returns:
            str: returns a representation of the email
        """
        return self.email

class ContactList:
    #A class which stores attributes relating to an Contact List
     
    def __init__(self):
        """Initializes an Contact List object
    
            Attributes:
                list: define a dictionary in a list of contacts objects
        """
        self.contacts = {}

    def add_contact(self, contact):
        """Adding a contact to the Contact List 
    
            Attributes:
                contact(str): the contact in which you are making
        """
        self.contacts[contact.first_name] = contact

    def remove_contact(self, first_name):
        """Removing a contact off the Contact List 
    
            Attributes:
                first_name(str): the first name of the person you're creating a contact for
        """
        if first_name in self.contacts:
            del self.contacts[first_name]
        else:
            messagebox.showerror("Contact not found", "Contact not found")

    def get_all_contacts(self):
        """Represent all the contacts you've made 
        
        Returns:
            str: returns a representation of the contacts
        """
        return self.contacts.values()

class ContactListApp:
     
        
    def __init__(self, root):
        """Initializes an Contact List App object
    
            Attributes:
                root (str): the top level directory of the Contact List App 
        """
        self.root = root
        self.root.geometry("300x200")
        self.root.title('Contact List App')
        self.contact_list = ContactList()

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Username").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password").pack()
        self.password_entry = tk.Entry(self.frame)
        self.password_entry.pack()
        
        tk.Button(self.frame, text="Login", command=self.login).pack()
        tk.Button(self.frame, text="Signup", command=self.signup).pack()
    
    def login(self):
        """The login screen in which the user is able to sign in 
    
            Attributes:
                username(str): the username of the user 
                password(str): the password of the user
        """
        global username
        global password
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        #print(username)
        path = "login_list.txt"
        
        def login_checker(path, username, password):
            """Checks to see if the username and password matches and if they match then allows user to log in
    
            Attributes:
                path (str): the path of the file
                username(str): the username of the user 
                password(str): the password of the user
            """
            with open(path, 'r') as login_list:
                login_list_content = login_list.read()
                users = login_list_content.split("End Login\n")
                for user in users:
                    lines = user.strip().split("\n")
                    if len(lines) >= 2:
                        existing_username = lines[0].split(":")[1].strip()
                        existing_password = lines[1].split(":")[1].strip()
                        if existing_username == username and existing_password == password:
                            return True  # Username and password match
                return False  # Username or password does not match
            
        if login_checker(path, username, password) == True:
            self.frame.destroy()
            
            self.contacts_frame = tk.Frame(self.root)
            self.contacts_frame.pack()

            self.add_contact_button = tk.Button(self.contacts_frame, text="Add Contact", command=self.add_contact)
            self.add_contact_button.pack()

            self.remove_contact_button = tk.Button(self.contacts_frame, text="Remove Contact", command=self.remove_contact)
            self.remove_contact_button.pack()

            self.show_contacts_button = tk.Button(self.contacts_frame, text="Show Contacts", command=self.show_contacts)
            self.show_contacts_button.pack()
        else:
            messagebox.showerror("Error", "Invalid username or password")
        
    def get_user(self):
        """Gets the user their information 
    
            Returns:
                username(str): returns a representation of the username
        """
        
        username = self.username_entry.get()
        return username
            
    def signup(self):
        """Lets the user sign up to make an account
        
        Returns:
            str: returns a representation of the username
        """
        self.signup_window = tk.Toplevel()
        self.signup_window.geometry("300x200")
        self.signup_window.title("Signup")
        
        tk.Label(self.signup_window, text="Username").pack()
        
        self.username_signup_entry = tk.Entry(self.signup_window)
        self.username_signup_entry.pack()
        
        tk.Label(self.signup_window, text="Password").pack()
        
        self.password_signup_entry = tk.Entry(self.signup_window, show="*")
        self.password_signup_entry.pack()
        
        def login_checker(path, user):
            """Checks to see if the username and password matches and if they match then allows user to log in
    
            Attributes:
                path (str): the path of the file
                user(str): the user logging in
            """
            with open(path, 'r') as login_list:
                for line in login_list:
                    if line.startswith("Username:"):
                        existing_username = line.split(":")[1].strip()
                    if existing_username == user:
                        return False
                return True
            
        def signup_save():
            """Lets the user save the information they used during sign up
            """
            username = self.username_signup_entry.get()
            password = self.password_signup_entry.get()
            
            path = 'login_list.txt'
        
            if login_checker(path, username) == True:
                user = {"username": username, "password": password}
    
                with open(path, 'a') as login_list:
                    login_list.write(f"Username: {user['username']}\n")
                    login_list.write(f"Password: {user['password']}\n")
                    login_list.write("End Login\n")
            else:
                messagebox.showerror("Error", "Username already exist")
                
            self.signup_window.destroy()
                
        tk.Button(self.signup_window, text="Done", command=signup_save).pack()

    def run(self):
        """Lets the main function run
        """
        self.root.mainloop()

    def add_contact(self):
        """Adds contact to the Contact List
        """
        add_contact_window = tk.Toplevel(self.root)
        add_contact_window.title("Add Contact")
        add_contact_window.geometry("300x300")

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
            """Saves the contact to the Contact List
            """
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone_number = phone_entry.get()
            email = email_entry.get()
            contact = Contact(first_name, last_name, phone_number, email)
            self.contact_list.add_contact(contact)
            
            
            owner = username
            
            path = 'login_list.txt'
            with open(path, 'a') as contact_list_txt:
                contact_list_txt.write(f"Contact of {owner} -- First Name: {first_name}\n")
                contact_list_txt.write(f"Last Name: {last_name}\n")
                contact_list_txt.write(f"Phone Number: {phone_number}\n")
                contact_list_txt.write(f"Email: {email}\n")
                contact_list_txt.write("End Contact\n")
            
            messagebox.showinfo("Add Contact", "Contact added successfully")
            add_contact_window.destroy()

        save_button = tk.Button(add_contact_window, text="Save", command=save_contact)
        save_button.pack()

    def remove_contact(self):
        """Removes contact off the Contact List
        """
        remove_contact_window = tk.Toplevel(self.root)
        remove_contact_window.title("Remove Contact")
        remove_contact_window.geometry("300x200")

        first_name_label = tk.Label(remove_contact_window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(remove_contact_window)
        first_name_entry.pack()

        def remove():
            """Removes contact from the Contact List
            """
            first_name = first_name_entry.get()
            self.contact_list.remove_contact(first_name)
            remove_contact_window.destroy()

        remove_button = tk.Button(remove_contact_window, text="Remove", command=remove)
        remove_button.pack()
   
  
   
    def show_contacts(self):
        """Shows the user all the contacts that is available to them 
    
            Returns:
                (str): returns a representation of the contact list 
        """
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
        """Lets the main function run
        """
        self.root.mainloop()

if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    root = tk.Tk()
    app = ContactListApp(root)
    app.run()


"""
End of Main code--------------------------------------------------------"""

