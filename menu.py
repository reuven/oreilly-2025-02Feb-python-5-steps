def menu(list_of_options):
    while True:
        user_choice = input(f'Choose from {list_of_options}: ').strip()
    
        if user_choice in list_of_options:
            return user_choice
    
        print(f'{user_choice} is invalid; try again')
