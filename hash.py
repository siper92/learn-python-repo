import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    print(salt)
    print("Password encoded {0}".format(password.encode()))
    print("Salt {0}".format(salt))
    print("Salt encoded {0}".format(salt.encode()))
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')

# grape -> 0f78fcc486f5315418fbf095e71c0675ee07d318e5ac4d150050cd8e57966496
print("Grape is: {0}".format(hashlib.sha256("grape".encode()).hexdigest()))