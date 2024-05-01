contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        print("This name already exists")
    else:
        contacts[name] = phone    
        print("Contact added.") 

def show_phone(args, contacts):
    try:    
        name = args[0]  
        if name in contacts:
            print(contacts[name])
        else:
            print("There is no such contact")          
    except Exception as e:
        print(e)
        

def change_contact(args, contacts):
    try:
        name, phone = args    
        if name in contacts:
            contacts[name] = phone           
            print("Contact update.") 
        else:
            print("There is no such contact")
    except Exception as e:
        print(e)

def show_all(contacts):
    if  len(contacts) > 0:
        for key, value in contacts.items():
            print(key, ":", value)
    else:
        print("No contacts yet")
    



def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "add":
            add_contact(args, contacts)

        elif command == "phone":
            show_phone(args, contacts)

        elif command == "change":
            change_contact(args, contacts)

        elif command == "all":
            show_all(contacts)

        elif command == "hello":
            print("How can I help you?")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


