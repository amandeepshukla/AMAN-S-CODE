class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contacts found.")

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 < index <= len(self.contacts):
            if name:
                self.contacts[index - 1]['name'] = name
            if phone:
                self.contacts[index - 1]['phone'] = phone
            if email:
                self.contacts[index - 1]['email'] = email
            if address:
                self.contacts[index - 1]['address'] = address
            print("Contact updated.")
        else:
            print("Invalid contact number.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            removed_contact = self.contacts.pop(index - 1)
            print(f"Contact '{removed_contact['name']}' deleted.")
        else:
            print("Invalid contact number.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            index = int(input("Enter contact number to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(index, name, phone, email, address)
        elif choice == "5":
            index = int(input("Enter contact number to delete: "))
            contact_book.delete_contact(index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()