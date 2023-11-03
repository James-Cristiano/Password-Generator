#Password Generator 
import string
import random

#setting length of password
Length = int(input('Enter length of the password you would like: '))
#while True:  
#        PassLength = Length
#        if int(PassLength) < 8: 
#            print('Secure passwords must be more than 8 characters.')
#            Length = input('Please enter a new length for the password: ')
#        else:
#            break

#getting what characters are needed for the password
CharacterList = ""
print('''Choose the character sets required for the password: 
            1. Letters
            2. Digits
            3. Special Characters
            4. Finished''')
while True: 
    Choice = int(input('Pick a number: '))
    if Choice == 1:
        CharacterList += string.ascii_letters
    elif Choice == 2:
        CharacterList += string.digits
    elif Choice == 3:
        CharacterList += string.punctuation
    elif Choice ==4:
        break
    else: 
        print('Please pick one of the available options.')

#setting the password
Password = []
for i in range(Length):
    RandomChar = random.choice(CharacterList)
    Password.append(RandomChar)

#Giving user their password
print('Your random password is: ' + "".join(Password))