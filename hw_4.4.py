def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Not enough data. Use: add name phone"
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Not enough data. Use: change name phone"
    name = args[0]
    phone = args[1]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Please enter a name. Use: phone name"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts yet."
    result_lines = []
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")
    return "\n".join(result_lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            message = add_contact(args, contacts)
            print(message)
        elif command == "change":
            message = change_contact(args, contacts)
            print(message)
        elif command == "phone":
            message = show_phone(args, contacts)
            print(message)
        elif command == "all":
            message = show_all(contacts)
            print(message)
        elif command == "":
            print("Please enter a command.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()