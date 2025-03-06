import string
import random
def password_generator(size=12, chars=string.ascii_lowercase+string.ascii_uppercase+string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

print(password_generator()) 
