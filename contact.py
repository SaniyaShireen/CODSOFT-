class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("contacts not available.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("contacts not found.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone if new_phone else contact.phone
                contact.email = new_email if new_email else contact.email
                print(f"Updated contact: {contact} sucessfully ✔️")
                return
        print("Contact not found. ❌")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"contact has been Deleted: {name} sucessfully!✔️")
                return
        print("Contact not found.❌")


def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("choose (1). for Add Contact")
        print("choose (2). for. View Contacts")
        print("choose (3). for. Search Contact")
        print("choose (4). for. Update Contact")
        print("choose (5). for. Delete Contact")
        print("choose (6). for. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone to search: ")
            manager.search_contact(query)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            manager.update_contact(name, new_phone or None, new_email or None)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting the program. Thankyou ❤️")
            break
        else:
            print("Invalid choice. please try again 😵‍💫")

if __name__ == "__main__":
    main()


        
            






