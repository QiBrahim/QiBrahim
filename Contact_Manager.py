
contacts = [
    {
        'name': 'Amal',
        'number': '1111111111'
    },
    {
        'name': 'Mohammed',
        'number': '2222222222'
    },
    {
        'name': 'Khadijah',
        'number': '3333333333'
    },
    {
        'name': 'Abdullah',
        'number': '4444444444'
    },
    {
        'name': 'Rawan',
        'number': '5555555555'
    },
    {
        'name': 'Faisal',
        'number': '6666666666'
    },
    {
        'name': 'Layla',
        'number': '7777777777'
    }
]

def is_valid_number(number):
    return True if len(number) == 10 and number.isdigit() else False

def show_all_contacts_info():
    for i in contacts:
        print('name: '+ i['name'] +' | Phone Number:' + i['number'])


def add_new_contact(name, number):
    for i in contacts:
        # check is name is exist
        if name in i['name']:
            print('Failed, This name is exist, please Enter another name')
        # check is number is exist
        if number in i['number']:
            print('number', 'Failed, This number is exist')
    # add contact
    contacts.append({'name': name, 'number': number})
    print('Success')
    print('name: ' + name + ' | Phone Number:' + number)


def get_contact_info_from_name(name):
    for i in contacts:
        if name in i['name'] or name in i['name'].lower():
            return 'name:' + i['name'] + ' | phone number:' + i['number']
    return 'Sorry, the number for this name is not found'


def get_contact_info_from_number(num):
    # get the number holder name ...
    for i in contacts:
        # if number in the numbers book dic ...
        if i['number'] == num:
            return 'name:' + i['name'] + ' | phone number:' + i['number']
    # if number is not found ...
    return 'Sorry, the number is not found'


def menu():
    while True:
        print("Contact Manager: Choose 1 of 5 choices")
        print("1 - search by Number")
        print("2 - search by Name")
        print("3 - Show all Contacts")
        print("4 - add a new Contact")
        print("5 - exit")
        choice = input("Please make a choice: ")

        # search by Number
        if choice == "1":
            while True:
                number = input('Enter contact phone number: ')
                if not is_valid_number(number):
                    print('Please enter a valid phone number')
                else:
                    break
            print()
            print(get_contact_info_from_number(number))
            print()

        # search by Name
        elif choice == "2":
            name = input('Enter contact name: ')
            print()
            print(get_contact_info_from_name(name))
            print()

        # show all Contacts
        elif choice == "3":
            print()
            show_all_contacts_info()
            print()

        # Add new Number
        elif choice == "4":
            print()
            while True:
                name = input('Enter contact name: ')
                number = input('Enter contact phone number: ')
                if not is_valid_number(number):
                    print('Please enter a valid phone number')
                elif name != "":
                    print('Please enter a valid name')
                else:
                    break
            print()
            add_new_contact(name, number)
            print()
        # Add new Number
        elif choice == "5":
            exit()
        else:
            print('Make a choice')
        input('Press Enter key to go back to menu')

menu()
