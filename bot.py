phone_book = []

def hello(user_input):
    print('How can I help you?')

def end_program(user_input):
    print('Good bye!')
    exit()

def add_contact(user_input):
    contact_name = user_input.split(' ')[1]
    contact_number = user_input.split(' ')[2]
    contact = {contact_name: contact_number}
    phone_book.append(contact)
    print(f'Contact {contact_name} with number {contact_number} has been added to the phonebook.')

def change_contact(user_input):
    contact_name = user_input.split(' ')[1]
    new_contact_number = user_input.split(' ')[2]
    for contact in phone_book:
        if contact_name in contact:
            phone_book[phone_book.index(contact)][contact_name] = new_contact_number
            return
    print(f'There is no contact named {contact_name}') #its printed only if contact has not been found

def display_phone(user_input):
    contact_name = user_input.split(' ')[1]
    for contact in phone_book:
        if contact_name in contact:
            print(contact[contact_name])
            return
    print(f'There is no contact named {contact_name}') #its printed only if contact has not been found

def show_all(user_input):
    for contact in phone_book:
        for contact_name, contact_number in contact.items():
            print(f'Name: {contact_name} Number: {contact_number}')

def unknown_command(user_input):
    print('Unknown command')

COMMANDS = {
    'hello': hello,
    '.': end_program,
    'close': end_program,
    'good bye': end_program,
    'exit': end_program,
    'add': add_contact,
    'zmien': change_contact,
    'phone': display_phone,
    'show all': show_all
}

def get_handler(user_input):
    """Functions checks user input and return appropiate functions if correct command had been entered."""
    for command in COMMANDS.keys(): #iterate through commands
        if user_input.lower().startswith(command): #checks if user input starts with a knowns command
            return COMMANDS[command]
        else:
            continue
    return unknown_command #if there was no match it returns 'unknown command'

def main():
    while True:
        user_input = input('Enter your next command: ')
        handler = get_handler(user_input)
        handler(user_input)
        print(phone_book)
        
if __name__ == '__main__':
    main()