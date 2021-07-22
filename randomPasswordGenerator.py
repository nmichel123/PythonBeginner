#import modules
import random
import string

print('\nHello, welcome to The Password Generator...')

#ask user for length of password
length = int(input('\nInput Length of Password: '))

#define data sets
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

#combine data
all = lowerCase + upperCase + numbers + symbols

#randomly select characters
rand = random.sample(all,length)

#create password
password = ''.join(rand)

print(password)