from typing import List, Dict, Tuple, Union

Contact = Dict[str, Union[str, int, bool]]

contacts: List[Contact] = []


def add_contact(name: str, phone: int, email: str, favorite: bool = False) -> None:
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite
    }
    contacts.append(contact)


def get_contact(name: str) -> Contact:
    for contact in contacts:
        if contact["name"] == name:
            return contact
    raise ValueError("Contact not found")


def get_all_contacts() -> List[Contact]:
    return contacts


def get_favorite_contacts() -> List[Contact]:
    return [contact for contact in contacts if contact["favorite"]]


def update_contact(name: str, phone: int, email: str, favorite: bool = False) -> None:
    contact_name = input("Name of the contact to update: ")
    for contact in contacts:
        if contact["name"] == contact_name:
            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            contact["favorite"] = favorite
            return
    raise ValueError("Contact not found")


def delete_contact(name: str) -> None:
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            contacts.pop(i)
            return
    raise ValueError("Contact not found")


def menu():
    print("1. Add contact")
    print("2. Get contact")
    print("3. Get all contacts")
    print("4. Get favorite contacts")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Exit")
    return int(input("Choose an option: "))


def main():
    while True:
        option = menu()
        if option == 1:
            name = input("Name: ")
            phone = int(input("Phone: "))
            email = input("Email: ")
            favorite = input("Favorite (y/n): ").lower() == "y"
            add_contact(name, phone, email, favorite)
        elif option == 2:
            name = input("Name: ")
            print(get_contact(name))
        elif option == 3:
            print(get_all_contacts())
        elif option == 4:
            print(get_favorite_contacts())
        elif option == 5:
            name = input("Name: ")
            phone = int(input("Phone: "))
            email = input("Email: ")
            favorite = input("Favorite (y/n): ").lower() == "y"
            update_contact(name, phone, email, favorite)
        elif option == 6:
            name = input("Name: ")
            delete_contact(name)
        elif option == 7:
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
