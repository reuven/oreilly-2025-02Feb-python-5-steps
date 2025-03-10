def menu(list_of_options):
    while True:
        user_choice = input(f'Choose from {list_of_options}: ').strip()
    
        if user_choice in list_of_options:
            return user_choice
    
        print(f'{user_choice} is invalid; try again')

if __name__ == '__main__':
    user_choice = menu(['a', 'b', 'c'])
    print(f'You chose {user_choice}')
