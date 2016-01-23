def ask_number(guess_number, the_number):
    ''' Ask for a number.'''
    response = None
    if guess_number < the_number:
        print("Higher...")
    else:
        print("Lower...")
    response = guess_number
    return response
