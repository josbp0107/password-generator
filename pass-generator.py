import random
import string

def generate_password():
    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    simbols = list(string.punctuation)
    numbers = list(string.digits)

    characters = mayus + minus + simbols + numbers

    password = []

    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)
    
    password = "".join(password)

    return password



def run():
    password = generate_password()
    print('You new password is: ' + password)
    


if __name__ == "__main__":
    run()