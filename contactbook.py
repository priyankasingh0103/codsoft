import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Manager")
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
        
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts available!")
        else:
            contact_list = "\n".join([f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        
    def search_contact(self):
        query = self.search_entry.get().lower()
        found_contacts = []
        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone.lower():
                found_contacts.append(contact)
        if found_contacts:
            contact_list = "\n".join([f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("No Results", "No contacts found.")
    
    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            for contact in self.contacts:
                if contact.name == name or contact.phone == phone:
                    contact.name = name
                    contact.phone = phone
                    contact.email = email
                    contact.address = address
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Contact", "Contact not found!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
    
    def delete_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        
        if name and phone:
            for contact in self.contacts:
                if contact.name == name or contact.phone == phone:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Contact", "Contact not found!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
