# Email Validation Mini Project with Python:

# Some Rule with is Must necessary for a right mail.
'''
1. At least 6 charactor should in email. ex. k@k.in
2. Index[0] should alphabet.
3. In email @ should @ == 1:
4. In your email the (.) should in the position of index [-4] ^ [-3]
5. space not allow in email.
6. capital alphabetic not allow in email, all alphabetic should lower.
7. digits allowed.
8. you can't use special character in email. only '@' allowed.

'''

while True:
    email = input("enter you email: ")
    k, j, d = 0, 0, 0

    if email.lower() == 'e':
        break  # Exit the loop if user inputs 'e'

    if len(email) >= 6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@') == 1):
                if (email[-4] == '.') ^ (email[-3] == '.'): # ^ is a bitwise XOR operator

                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.isupper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == '_' or i == '.' or i == '@':
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        print("Wrong Email 5")
                    else:
                        print("Right Email")
                else:
                    print("Wrong email 4")
            else:
                print("Wrong email 3")
        else:
            print("Wrong email 2")
    else:
        print("wrong email 1")


print("Thank You")

