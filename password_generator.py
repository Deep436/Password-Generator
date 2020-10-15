## Password generator
import random
import string

s1 = string.ascii_letters
s2 = string.hexdigits
s3 = string.punctuation
s4 = string.punctuation
s5 = string.ascii_letters
s6 = string.punctuation

while True:
    print('\nTo exit the program ? Press 1')
    plength = int(input("Enter length of the password  : "))
    if plength == 1:
        print("Thanks for using password generator ??")
        break
    elif plength>5:
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        s.extend(list(s5))
        s.extend(list(s6))
        # print(s)

        random.shuffle(s) ## Just like tash ka pattta
        
        # random.sample(s,plength)  ## We can also use this 
        print(f'\nPlease try this password  : {"".join(s[0:plength])}')
    else: 
        print("\nYour password contain very less digit please increase the value ... ?\n")