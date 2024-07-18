import string , random

def generate_password(length , special , letters , digits):
    str =''
    if special:
        str_special = list("@#$%^&*()!~")
        str+=random.choice(str_special)
        str+=random.choice(str_special)
        length=length-2
    if letters:
        str_uppercase=list(string.ascii_uppercase)
        str +=random.choice(str_uppercase)
        str +=random.choice(str_uppercase)
        length=length-2
    if digits:
        str_digits= list(string.digits)
        str+=random.choice(str_digits)
        str+=random.choice(str_digits)
        length=length-2
    if letters:
        str_lowercase=list(string.ascii_lowercase)
        while length>0:
          str +=random.choice(str_lowercase) 
          length=length-1

        
    try:
        password = ''
        char_list=list(str)
        random.shuffle(char_list)
        password =''.join(char_list)
        print(password)
        return password
    except ValueError as e:
        print(f"Error generating password: {e}")
        return None
        
def get_password_length():
    while True:
        try:
            length = int(input("Enter length of Password: "))
            if length <= 0:
                raise ValueError("Length must be greater than zero.")
            elif length < 8:
                raise ValueError("Length must be between 8 and 12 for a strong password.")
            return length
        except ValueError as e:
            print(f'Error: {e}. Please enter a valid length.')

print('The password generated will have 2 special_character, 2 capital_letter if chosen, and remaining a combination of numbers and lowercase characters.')

length = get_password_length()
special = input("Do you want special characters in your Password: ").lower() == 'yes'
letters = input("Do you want letters in your Password: ").lower() == 'yes'
digits = input("Do you want numeric values in your Password:  ").lower() == 'yes'
password = generate_password(length, special, letters, digits)
if password:
     print("Generated Password:", password)
else:
    print("Failed to generate password.")